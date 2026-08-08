#ifndef SERIAL_HANDLER_H
#define SERIAL_HANDLER_H

#include <Arduino.h>

class SerialHandler
{
public:
    explicit SerialHandler(unsigned long baudRate);

    void begin();
    bool available() const;
    String readCommand();

private:
    unsigned long _baudRate;
};

#endif