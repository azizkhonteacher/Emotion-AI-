#include <MD_MAX72xx.h>
#include <SPI.h>

#include "config.h"
#include "display.h"
#include "emoji.h"
#include "protocol.h"
#include "serial_handler.h"

MD_MAX72XX matrix(
    HARDWARE_TYPE,
    PIN_DATA,
    PIN_CLK,
    PIN_CS,
    MAX_DEVICES
);

Display display(matrix);
SerialHandler serialHandler(115200);
Emotion currentEmotion = Emotion::Unknown;


const Emoji* getEmoji(Emotion emotion)
{
    switch (emotion)
    {
        case Emotion::Happy:
            return &HAPPY;

        case Emotion::Sad:
            return &SAD;

        case Emotion::Angry:
            return &ANGRY;

        case Emotion::Neutral:
            return &NEUTRAL;

        case Emotion::Surprise:
            return &SURPRISE;

        case Emotion::Fear:
            return &FEAR;

        case Emotion::Disgust:
            return &DISGUST;

        case Emotion::Unknown:
        default:
            return nullptr;
    }
}


void setup()
{
    serialHandler.begin();

    display.begin(5);

    display.show(HAPPY);

    Serial.println("Matrix initialized.");
    Serial.println("System ready.");
}


void loop()
{
    if (!serialHandler.available())
    {
        return;
    }

    const String command = serialHandler.readCommand();

    Serial.print("Received: ");
    Serial.println(command);

    const Emotion emotion = parseEmotion(command);

    if (emotion == Emotion::Unknown)
    {
        Serial.print("Unknown emotion: ");
        Serial.println(command);

        return;
    }

    if (emotion == currentEmotion)
    {
        return;
    }

    const Emoji* emoji = getEmoji(emotion);

    if (emoji == nullptr)
    {
        Serial.print("Unsupported emotion: ");
        Serial.println(command);

        return;
    }

    display.show(*emoji);

    currentEmotion = emotion;

    Serial.print("Display updated: ");
    Serial.println(command);
}