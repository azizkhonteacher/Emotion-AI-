#ifndef CONFIG_H
#define CONFIG_H

#include <MD_MAX72XX.h>

// =========================
// MAX7219 Configuration
// =========================

constexpr MD_MAX72XX::moduleType HARDWARE_TYPE = MD_MAX72XX::FC16_HW;

constexpr uint8_t MAX_DEVICES = 1;

// SPI Pins
constexpr uint8_t PIN_DATA = 11;
constexpr uint8_t PIN_CLK = 12;
constexpr uint8_t PIN_CS = 10;

#endif