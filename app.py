import streamlit as st
import imageio
import PIL.Image

def main():
    st.title("Video Playback with imageio and Streamlit")

    video_file = st.sidebar.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

    if video_file is not None:
        stframe = st.empty()

        reader = imageio.get_reader(video_file)
        for frame in reader:
            img = PIL.Image.fromarray(frame)
            stframe.image(img)

            # Simula la velocidad de los fotogramas
            st.time.sleep(1/30)  # Ajusta según el FPS del video

if __name__ == "__main__":
    main()
