import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Video Capture with OpenCV and Streamlit")

    # Selección de la cámara
    cam_index = st.sidebar.selectbox("Seleccione la cámara", options=[0, 1, 2, 3], index=0)

    # Configuración de la cámara
    cap = cv2.VideoCapture(cam_index)

    if not cap.isOpened():
        st.error("No se pudo acceder a la cámara.")
        return

    stframe = st.empty()

    # Loop de captura de video
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("No se pudo leer el frame de la cámara.")
            break

        # Convertir el frame a formato compatible con Streamlit (RGB)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Mostrar el frame en Streamlit
        stframe.image(frame)

        # Salir del loop cuando el usuario cierre la aplicación
        if st.sidebar.button("Cerrar"):
            break

    # Liberar la cámara
    cap.release()

if __name__ == "__main__":
    main()
