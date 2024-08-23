import streamlit as st
import imageio
import PIL.Image

def main():
    st.title("Video Capture with imageio and Streamlit")

    # Configurar el dispositivo de la cámara
    camera = imageio.get_reader('<video0>')

    stframe = st.empty()

    while True:
        frame = camera.get_next_data()
        frame = PIL.Image.fromarray(frame)

        stframe.image(frame)

        if st.sidebar.button("Cerrar"):
            break

if __name__ == "__main__":
    main()
