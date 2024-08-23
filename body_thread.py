import mediapipe as mp
import cv2
import threading
import time
import global_vars
from clientUDP import ClientUDP
from capture_thread import CaptureThread

class BodyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.data = ""
        self.client = None
        self.capture_thread = None

    def run(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        self.setup_comms()

        self.capture_thread = CaptureThread()
        self.capture_thread.start()

        with mp_pose.Pose(min_detection_confidence=0.80, min_tracking_confidence=0.5,
                          model_complexity=global_vars.MODEL_COMPLEXITY, static_image_mode=False, enable_segmentation=True) as pose:

            while not global_vars.KILL_THREADS and self.capture_thread.isRunning == False:
                time.sleep(0.5)

            while not global_vars.KILL_THREADS and self.capture_thread.cap.isOpened():
                ret = self.capture_thread.ret
                image = self.capture_thread.frame

                image = cv2.flip(image, 1)
                image.flags.writeable = global_vars.DEBUG

                results = pose.process(image)

                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                self.data = ""
                if results.pose_world_landmarks:
                    for i, landmark in enumerate(results.pose_world_landmarks.landmark):
                        self.data += "{}|{}|{}|{}\n".format(i, landmark.x, landmark.y, landmark.z)

                self.send_data(self.data)

    def setup_comms(self):
        self.client = ClientUDP(global_vars.HOST, global_vars.PORT)

    def send_data(self, message):
        if not global_vars.USE_LEGACY_PIPES:
            self.client.send_message(message)
