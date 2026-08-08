#ifndef EMOJI_H
#define EMOJI_H

#include <stdint.h>

struct Emoji
{
    const uint8_t* bitmap;
};

extern const Emoji HAPPY;
extern const Emoji SAD;
extern const Emoji ANGRY;
extern const Emoji NEUTRAL;
extern const Emoji SURPRISE;
extern const Emoji FEAR;
extern const Emoji DISGUST;

#endif