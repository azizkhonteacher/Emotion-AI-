"""
Camera module.

Responsible only for camera operations.
"""

from __future__ import annotations

import cv2
import numpy as np

from config import (
    CAMERA_INDEX,
    FRAME_HEIGHT,
    FRAME_WIDTH,
)
from utils import setup_logger


logger = setup_logger(__name__)


class Camera:
    """
    Camera wrapper around OpenCV VideoCapture.
    """

    def __init__(self) -> None:
        """Initialize the camera."""
        self.cap = cv2.VideoCapture(CAMERA_INDEX)

        if not self.cap.isOpened():
            logger.error("Unable to open camera.")
            raise RuntimeError("Unable to open camera.")

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        logger.info("Camera initialized.")

    def read(self) -> np.ndarray:
        """
        Read one frame.

        Returns
        -------
        numpy.ndarray
            Camera frame.
        """

        success, frame = self.cap.read()

        if not success:
            logger.error("Failed to read frame.")
            raise RuntimeError("Failed to read frame.")

        return frame

    def release(self) -> None:
        """Release camera resources."""

        self.cap.release()
        cv2.destroyAllWindows()

        logger.info("Camera released.")