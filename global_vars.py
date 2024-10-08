import os

# Internally used, don't mind this.
KILL_THREADS = False

# Toggle this in order to view how your WebCam is being interpreted (reduces performance).
DEBUG = True

# Change UDP connection settings (must match Unity side)
USE_LEGACY_PIPES = False
HOST = '0.0.0.0'
PORT = int(os.getenv('PORT', 52733))

# Settings do not universally apply, not all WebCams support all frame rates and resolutions
CAM_INDEX = 0
USE_CUSTOM_CAM_SETTINGS = False
FPS = 60
WIDTH = 320
HEIGHT = 240

# [0, 2] Higher numbers are more precise, but also cost more performance. The demo video used 2 (good environment is more important).
MODEL_COMPLEXITY = 2
