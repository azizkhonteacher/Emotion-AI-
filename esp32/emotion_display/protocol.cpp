#include "protocol.h"

Emotion parseEmotion(const String& message)
{
    if (message == "HAPPY")
    {
        return Emotion::Happy;
    }

    if (message == "SAD")
    {
        return Emotion::Sad;
    }

    if (message == "ANGRY")
    {
        return Emotion::Angry;
    }

    if (message == "NEUTRAL")
    {
        return Emotion::Neutral;
    }

    if (message == "SURPRISE")
    {
        return Emotion::Surprise;
    }

    if (message == "FEAR")
    {
        return Emotion::Fear;
    }

    if (message == "DISGUST")
    {
        return Emotion::Disgust;
    }

    return Emotion::Unknown;
}