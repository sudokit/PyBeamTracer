import multiprocessing as mp
from .types import Point

# image
ASPECT_RATIO = 16.0 / 9.0
WIDTH = 400
HEIGHT = int(WIDTH / ASPECT_RATIO)
# camera
VIEWPORT_HEIGHT = 2.0
VIEWPORT_WIDTH = VIEWPORT_HEIGHT * (WIDTH / HEIGHT)
FOCAL_LENGTH = 1.0
CAMERA_CENTER = Point(0, 0, 0)
# threading
NUM_THREADS = max(round(mp.cpu_count() * 0.9), 2)