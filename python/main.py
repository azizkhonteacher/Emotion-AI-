"""
Application entry point.
"""

from __future__ import annotations

import cv2

from camera import Camera
from config import WINDOW_NAME
from utils import setup_logger
from face_detector import FaceDetector
from emotion_detector import EmotionDetector
from config import EMOTION_DETECTION_INTERVAL
from emotion_mapper import EmotionMapper
from serial_sender import SerialSender


logger = setup_logger(__name__)

def main() -> None:
    """
    Start the camera preview.
    """
    serial_sender = SerialSender()

    if not serial_sender.connect():
        logger.warning("ESP32 not connected. Running without serial.")

    camera = None

    try:
        logger.info("Application started.")

        camera = Camera()
        face_detector = FaceDetector()
        emotion_detector = EmotionDetector()
        
        frame_count = 0
        current_emotion = ""
        current_confidence = 0.0
        last_sent_emotion = None

        while True:
            frame = camera.read()
            
            faces = face_detector.detect(frame)
            
            frame_count += 1

            for (x, y, w, h) in faces:
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2,
                )
                
                if frame_count % EMOTION_DETECTION_INTERVAL == 0:
                    face_roi = frame[y:y + h, x:x + w]
                    result = emotion_detector.detect(face_roi)

                    if result is not None:
                        current_emotion, current_confidence = result

                if current_emotion:
                    # Ortiqcha qavs olib tashlandi
                    text = f"{current_emotion} ({current_confidence:.1f}%)"

                    cv2.putText(
                        frame,
                        text,
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2,
                    )
                
                mapped = EmotionMapper.map(current_emotion)

                if mapped != last_sent_emotion:
                    serial_sender.send(mapped.value)
                    last_sent_emotion = mapped

            cv2.imshow(WINDOW_NAME, frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                logger.info("Exit requested by user.")
                break

    except Exception as exc:
        logger.exception("Unexpected error: %s", exc)

    finally:
        # Dastur yakunlanganda barcha qurilmalar xavfsiz yopiladi
        if camera is not None:
            camera.release()
            
        serial_sender.close() # Portni yopish funksiya ichiga olib kirildi
        cv2.destroyAllWindows() # Ochiq qolgan darcha yopiladi
        
        logger.info("Application closed.")

if __name__ == "__main__":
    main()