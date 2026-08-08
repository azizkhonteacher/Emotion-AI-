#include "serial_handler.h"

SerialHandler::SerialHandler(unsigned long baudRate)
    : _baudRate(baudRate)
{
}

void SerialHandler::begin()
{
    Serial.begin(_baudRate);

    Serial.println("ESP32 Ready");
}

bool SerialHandler::available() const
{
    return Serial.available() > 0;
}

String SerialHandler::readCommand()
{
    String command = Serial.readStringUntil('\n');

    command.trim();

    return command;
}