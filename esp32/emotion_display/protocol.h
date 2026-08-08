#ifndef PROTOCOL_H
#define PROTOCOL_H

#include <Arduino.h>

enum class Emotion
{
    Happy,
    Sad,
    Angry,
    Neutral,
    Surprise,
    Fear,
    Disgust,
    Unknown
};

Emotion parseEmotion(const String& message);

#endif