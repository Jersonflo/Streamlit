import streamlit as st
from body_thread import BodyThread
import global_vars
import time

# Placeholder para el video
frame_placeholder = st.empty()

# Botones de control
if 'capture_active' not in st.session_state:
    st.session_state['capture_active'] = False

if st.button('Start Capture'):
    if not st.session_state['capture_active']:
        st.session_state['capture_active'] = True
        global_vars.KILL_THREADS = False
        body_thread = BodyThread()
        body_thread.start()

if st.button('Stop Capture'):
    if st.session_state['capture_active']:
        global_vars.KILL_THREADS = True
        st.session_state['capture_active'] = False
        time.sleep(0.5)

# Mostrar el video (esto es solo un placeholder; actualiza el contenido)
if st.session_state['capture_active']:
    st.write("Capturing video...")
else:
    st.write("Capture stopped.")
