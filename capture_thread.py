import cv2
import threading
import time
import global_vars

class CaptureThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.cap = None
        self.ret = None
        self.frame = None
        self.isRunning = False
        self.counter = 0
        self.timer = 0.0

    def run(self):
        self.cap = cv2.VideoCapture(global_vars.CAM_INDEX)
        if global_vars.USE_CUSTOM_CAM_SETTINGS:
            self.cap.set(cv2.CAP_PROP_FPS, global_vars.FPS)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, global_vars.WIDTH)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, global_vars.HEIGHT)

        time.sleep(1)

        while not global_vars.KILL_THREADS:
            self.ret, self.frame = self.cap.read()
            self.isRunning = True
            if global_vars.DEBUG:
                self.counter += 1
                if time.time() - self.timer >= 3:
                    self.counter = 0
                    self.timer = time.time()

    def stop(self):
        global_vars.KILL_THREADS = True
        if self.cap:
            self.cap.release()
