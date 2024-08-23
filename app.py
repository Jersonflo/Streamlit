import cv2
import streamlit as st

def main():
    st.title("Video Capture with OpenCV and Streamlit")

    # Intentar capturar la cámara
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        st.error("No se pudo acceder a la cámara.")
        return

    stframe = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("No se pudo leer el frame de la cámara.")
            break

        # Convertir el frame a RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Mostrar el frame en Streamlit
        stframe.image(frame)

        # Salir del loop cuando el usuario cierre la aplicación
        if st.sidebar.button("Cerrar"):
            break

    cap.release()

if __name__ == "__main__":
    main()
