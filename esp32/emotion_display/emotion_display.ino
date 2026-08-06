#include <SPI.h>
#include <MD_MAX72XX.h>

#include "config.h"
#include "emoji.h"

MD_MAX72XX matrix(
    HARDWARE_TYPE,
    PIN_DATA,
    PIN_CLK,
    PIN_CS,
    MAX_DEVICES
);

void setup()
{
    Serial.begin(115200);

    matrix.begin();

    matrix.control(MD_MAX72XX::INTENSITY, 5);

    matrix.clear();

    Serial.println("Matrix initialized.");

    // Hardware Test
    for (uint8_t row = 0; row < 8; row++)
    {
        for (uint8_t col = 0; col < 8; col++)
        {
            matrix.setPoint(row, col, true);
        }
    }

    matrix.update();
    drawBitmap(HAPPY);
}


void drawBitmap(const uint8_t bitmap[8])
{
    matrix.clear();

    for (uint8_t row = 0; row < 8; row++)
    {
        for (uint8_t col = 0; col < 8; col++)
        {
            bool pixel = bitRead(bitmap[row], 7 - col);
            matrix.setPoint(row, col, pixel);
        }
    }

    matrix.update();
}

void loop()
{
}