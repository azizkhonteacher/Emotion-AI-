#include "display.h"

Display::Display(MD_MAX72XX& matrix)
    : _matrix(matrix)
{
}

void Display::begin(uint8_t intensity)
{
    _matrix.begin();
    _matrix.control(MD_MAX72XX::INTENSITY, intensity);
    clear();
}

void Display::clear()
{
    _matrix.clear();
    _matrix.update();
}

void Display::show(const Emoji& emoji)
{
    if (emoji.bitmap == nullptr)
    {
        clear();
        return;
    }

    drawBitmap(emoji.bitmap);
}

void Display::showBitmap(const uint8_t bitmap[8])
{
    if (bitmap == nullptr)
    {
        clear();
        return;
    }

    drawBitmap(bitmap);
}

void Display::drawBitmap(const uint8_t bitmap[8])
{
    _matrix.clear();

    for (uint8_t row = 0; row < 8; row++)
    {
        for (uint8_t col = 0; col < 8; col++)
        {
            const bool pixel = bitRead(bitmap[row], 7 - col);

            _matrix.setPoint(row, col, pixel);
        }
    }

    _matrix.update();
}