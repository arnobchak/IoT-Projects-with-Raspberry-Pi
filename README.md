# IoT Projects with Raspberry Pi 3 Model B

This repository contains projects leveraging the Raspberry Pi 3 Model B for IoT applications. The projects demonstrate how to integrate and use various components, such as an ultrasonic sensor, DHT11 temperature and humidity sensor, LEDs, breadboard, push buttons, and resistors, programmed using Python. The repository is designed for beginners and intermediate users interested in learning IoT with Raspberry Pi.

## Table of Contents

- [Overview](#overview)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Project Features](#project-features)
- [Setup and Installation](#setup-and-installation)
- [Project Details](#project-details)
  - [1. Distance Measurement with Ultrasonic Sensor](#1-distance-measurement-with-ultrasonic-sensor)
  - [2. Temperature and Humidity Monitoring with DHT11](#2-temperature-and-humidity-monitoring-with-dht11)
  - [3. LED Control with Push Button](#3-led-control-with-push-button)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository showcases three primary IoT projects using the Raspberry Pi 3 Model B. Each project is designed to teach the integration of hardware components and Python programming for IoT solutions.

## Hardware Requirements

- Raspberry Pi 3 Model B
- Ultrasonic Sensor (HC-SR04)
- DHT11 Temperature and Humidity Sensor
- LED (any color)
- Breadboard
- Push Button
- Resistor (1kΩ or 10kΩ, as required)
- Jumper Wires
- 5V Power Supply for Raspberry Pi

## Software Requirements

- Raspbian OS (Bullseye or later)
- Python 3
- Libraries: `RPi.GPIO`, `Adafruit_DHT`
- SSH Client (e.g., PuTTY) or Monitor, Keyboard, and Mouse for Raspberry Pi

## Project Features

- Real-time distance measurement using an ultrasonic sensor.
- Temperature and humidity monitoring using DHT11.
- LED toggling with a push button.
- Simple Python programs to control and interact with the hardware.

## Setup and Installation

1. **Prepare Raspberry Pi:**

   - Install Raspbian OS on the Raspberry Pi.
   - Ensure Python 3 and required libraries are installed (`pip install RPi.GPIO Adafruit_DHT`).

2. **Hardware Connections:**

   - Connect each component to the Raspberry Pi GPIO pins according to the circuit diagrams provided in each project's folder.

3. **Clone the Repository:**

   ```bash
   git clone https://github.com/arnobchak/IoT-Projects-with-Raspberry-Pi.git
   cd IoT-Projects-with-Raspberry-Pi
   ```

4. **Run Python Programs:**
   Navigate to the project directory and execute the respective Python scripts using:

   ```bash
   python3 <script_name>.py
   ```

## Project Details

### 1. Distance Measurement with Ultrasonic Sensor

- **Objective:** Measure the distance of an object from the sensor and display it on the console.
- **Components:** HC-SR04, Raspberry Pi, Resistor (optional, for stable signal).
- **Code File:** `ultrasonic_sensor.py`
- **Working:** The sensor sends ultrasonic waves and calculates the time taken for the echo to return, determining the distance.

### 2. Temperature and Humidity Monitoring with DHT11

- **Objective:** Read temperature and humidity data and display it on the console.
- **Components:** DHT11 sensor, Raspberry Pi, Resistor (for stable data signal).
- **Code File:** `dht11_sensor.py`
- **Working:** The DHT11 sensor measures ambient temperature and humidity and sends the data to the Raspberry Pi.

### 3. LED Control with Push Button

- **Objective:** Toggle an LED on or off using a push button.
- **Components:** LED, push button, resistor (to limit current to the LED), breadboard, Raspberry Pi.
- **Code File:** `led_control.py`
- **Working:** The push button's state is read to turn the LED on or off.

## Future Enhancements

- Add a web interface for real-time data visualization.
- Integrate MQTT for remote monitoring.
- Expand the project with additional sensors (e.g., light sensors, air quality sensors).

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. Ensure your code follows best practices and includes appropriate comments.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

