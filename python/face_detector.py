"""
Face detection module.
"""

from __future__ import annotations

import cv2
import numpy as np

from utils import setup_logger

logger = setup_logger(__name__)


class FaceDetector:
    """
    Detect faces using OpenCV Haar Cascade.
    """

    def __init__(self) -> None:
        cascade_path = (
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        self.detector = cv2.CascadeClassifier(cascade_path)

        if self.detector.empty():
            logger.error("Failed to load Haar Cascade.")
            raise RuntimeError("Failed to load Haar Cascade.")

        logger.info("Face detector initialized.")

    def detect(
        self,
        frame: np.ndarray,
    ) -> list[tuple[int, int, int, int]]:
        """
        Detect faces in a frame.

        Returns
        -------
        list[(x, y, w, h)]
        """

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60),
        )

        return list(faces)