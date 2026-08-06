"""
Project configuration.

This module stores all configurable values used across the project.
Keeping them in one place makes maintenance easier.
"""

from pathlib import Path

# ------------------------------------------------------------------
# Project paths
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = PROJECT_ROOT / "assets"
MODELS_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"

# ------------------------------------------------------------------
# Camera settings
# ------------------------------------------------------------------

CAMERA_INDEX: int = 1
FRAME_WIDTH: int = 640
FRAME_HEIGHT: int = 480
WINDOW_NAME: str = "Emotion Detection"

# ------------------------------------------------------------------
# Serial settings
# ------------------------------------------------------------------

SERIAL_PORT: str = "COM4"
BAUD_RATE: int = 115200
SERIAL_TIMEOUT: float = 1.0

# ------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------

LOG_LEVEL: str = "INFO"

# ------------------------------------------------------------------
# Supported emotions
# ------------------------------------------------------------------

SUPPORTED_EMOTIONS: tuple[str, ...] = (
    "happy",
    "sad",
    "neutral",
    "angry",
    "surprise",
)

# ------------------------------------------------------------------
# AI
# ------------------------------------------------------------------

EMOTION_DETECTION_INTERVAL: int = 5