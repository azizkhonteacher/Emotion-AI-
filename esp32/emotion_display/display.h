#ifndef DISPLAY_H
#define DISPLAY_H

#include <MD_MAX72XX.h>

#include "emoji.h"

class Display
{
public:
    explicit Display(MD_MAX72XX& matrix);

    void begin(uint8_t intensity = 5);
    void show(const Emoji& emoji);
    void showBitmap(const uint8_t bitmap[8]);
    void clear();

private:
    MD_MAX72XX& _matrix;

    void drawBitmap(const uint8_t bitmap[8]);
};

#endif