"""
Serial communication module.
"""

from __future__ import annotations

import serial
from serial import SerialException

from config import BAUD_RATE, SERIAL_PORT, SERIAL_TIMEOUT
from utils import setup_logger

logger = setup_logger(__name__)


class SerialSender:
    """
    Send data to ESP32 over Serial.
    """

    def __init__(self) -> None:
        self.serial = None

    def connect(self) -> bool:
        """
        Open serial connection.

        Returns
        -------
        bool
            True if connection succeeded.
        """

        try:
            self.serial = serial.Serial(
                port=SERIAL_PORT,
                baudrate=BAUD_RATE,
                timeout=SERIAL_TIMEOUT,
            )

            logger.info(
                "Connected to %s (%d baud).",
                SERIAL_PORT,
                BAUD_RATE,
            )

            return True

        except SerialException as exc:
            logger.error("Serial connection failed: %s", exc)
            return False

    def send(self, message: str) -> bool:
        """
        Send text message.

        Parameters
        ----------
        message : str
            Message to send.
        """

        if self.serial is None:
            logger.warning("Serial port is not connected.")
            return False

        try:
            self.serial.write(f"{message}\n".encode("utf-8"))
            logger.info("Sent: %s", message)
            return True

        except SerialException as exc:
            logger.error("Serial send failed: %s", exc)
            return False

    def close(self) -> None:
        """
        Close serial connection.
        """

        if self.serial is not None and self.serial.is_open:
            self.serial.close()
            logger.info("Serial connection closed.")