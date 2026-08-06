"""
Utility functions for the Emotion Face project.
"""

from __future__ import annotations

import logging
from pathlib import Path

from config import LOG_LEVEL, LOGS_DIR


def setup_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger.

    Parameters
    ----------
    name : str
        Logger name (usually __name__).

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    # Ensure the logs directory exists
    Path(LOGS_DIR).mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)

    # Avoid duplicate handlers if called multiple times
    if logger.handlers:
        return logger

    logger.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File output
    file_handler = logging.FileHandler(
        LOGS_DIR / "emotion_face.log",
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger