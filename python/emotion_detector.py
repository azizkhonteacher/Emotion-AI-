"""
Emotion detection module.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
from deepface import DeepFace

from utils import setup_logger

logger = setup_logger(__name__)


class EmotionDetector:
    """
    Detect emotion from a face image.
    """

    def __init__(self) -> None:
        logger.info("Emotion detector initialized.")

    def detect(
        self,
        face: np.ndarray,
    ) -> Optional[tuple[str, float]]:
        """
        Detect dominant emotion.

        Parameters
        ----------
        face : np.ndarray
            Cropped face image.

        Returns
        -------
        tuple[str, float] | None
            (emotion, confidence)
        """

        try:
            result = DeepFace.analyze(
                img_path=face,
                actions=["emotion"],
                detector_backend="skip",
                enforce_detection=False,
                silent=True,
            )

            if isinstance(result, list):
                result = result[0]

            emotion = result["dominant_emotion"]
            confidence = result["emotion"][emotion]

            return emotion, confidence

        except Exception as exc:
            logger.exception("Emotion detection failed: %s", exc)
            return None