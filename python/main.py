"""
Application entry point.
"""

from __future__ import annotations

import cv2

from camera import Camera
from config import WINDOW_NAME
from utils import setup_logger


logger = setup_logger(__name__)


def main() -> None:
    """
    Start the camera preview.
    """

    camera = None

    try:
        logger.info("Application started.")

        camera = Camera()

        while True:
            frame = camera.read()

            cv2.imshow(WINDOW_NAME, frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                logger.info("Exit requested by user.")
                break

    except Exception as exc:
        logger.exception("Unexpected error: %s", exc)

    finally:
        if camera is not None:
            camera.release()

        logger.info("Application closed.")


if __name__ == "__main__":
    main()