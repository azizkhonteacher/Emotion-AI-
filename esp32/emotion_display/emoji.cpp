#include "emoji.h"

namespace
{
    // 😄 HAPPY
    const uint8_t HAPPY_BITMAP[8] =
    {
        0b00111100,
        0b01000010,
        0b10100101,
        0b10000001,
        0b10100101,
        0b10011001,
        0b01000010,
        0b00111100
    };

    // ☹ SAD
    const uint8_t SAD_BITMAP[8] =
    {
        0b00111100,
        0b01000010,
        0b10100101,
        0b10000001,
        0b10011001,
        0b10100101,
        0b01000010,
        0b00111100
    };

    // 😠 ANGRY
    const uint8_t ANGRY_BITMAP[8] =
    {
        0b00111100,
        0b01000010,
        0b10100101,
        0b10011001,
        0b10100101,
        0b10000001,
        0b01000010,
        0b00111100
    };

    // 😐 NEUTRAL
    const uint8_t NEUTRAL_BITMAP[8] =
    {
        0b00111100,
        0b01000010,
        0b10100101,
        0b10000001,
        0b10000001,
        0b10111101,
        0b01000010,
        0b00111100
    };

    // 😲 SURPRISE
    const uint8_t SURPRISE_BITMAP[8] =
    {
        0b00111100,
        0b01000010,
        0b10100101,
        0b10000001,
        0b10011001,
        0b10100101,
        0b01000010,
        0b00111100
    };

    // 😨 FEAR
    const uint8_t FEAR_BITMAP[8] =
    {
        0b00111100,
        0b01000010,
        0b10100101,
        0b10000001,
        0b10111101,
        0b10000001,
        0b01000010,
        0b00111100
    };

    // 🤢 DISGUST
    const uint8_t DISGUST_BITMAP[8] =
    {
        0b00111100,
        0b01000010,
        0b10100101,
        0b10000001,
        0b10111101,
        0b10011001,
        0b01000010,
        0b00111100
    };
}

const Emoji HAPPY =
{
    HAPPY_BITMAP
};

const Emoji SAD =
{
    SAD_BITMAP
};

const Emoji ANGRY =
{
    ANGRY_BITMAP
};

const Emoji NEUTRAL =
{
    NEUTRAL_BITMAP
};

const Emoji SURPRISE =
{
    SURPRISE_BITMAP
};

const Emoji FEAR =
{
    FEAR_BITMAP
};

const Emoji DISGUST =
{
    DISGUST_BITMAP
};