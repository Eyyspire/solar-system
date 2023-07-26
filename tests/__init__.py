import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
BODIES_PATH = os.path.join(
    SOURCE_PATH,"Bodies"
)

sys.path.append(SOURCE_PATH)
sys.path.append(BODIES_PATH)

