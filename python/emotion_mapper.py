"""
Emotion mapping module.
"""

from __future__ import annotations

from enum import Enum


class EmotionType(str, Enum):
    HAPPY = "HAPPY"
    SAD = "SAD"
    ANGRY = "ANGRY"
    NEUTRAL = "NEUTRAL"
    SURPRISE = "SURPRISE"
    FEAR = "FEAR"
    DISGUST = "DISGUST"
    UNKNOWN = "UNKNOWN"


class EmotionMapper:
    """
    Map DeepFace emotion names to ESP32 protocol values.
    """

    _MAP = {
        "happy": EmotionType.HAPPY,
        "sad": EmotionType.SAD,
        "angry": EmotionType.ANGRY,
        "neutral": EmotionType.NEUTRAL,
        "surprise": EmotionType.SURPRISE,
        "fear": EmotionType.FEAR,
        "disgust": EmotionType.DISGUST,
    }

    @classmethod
    def map(cls, emotion: str) -> EmotionType:
        """
        Convert DeepFace emotion string to EmotionType.
        """
        return cls._MAP.get(
            emotion.lower(),
            EmotionType.UNKNOWN,
        )