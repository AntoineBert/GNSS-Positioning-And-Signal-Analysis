# GNSS Real-Time Tracker & Geospatial Mapper

## 📌 Project Overview
This project implements a complete pipeline for GNSS data processing. It acquires raw **NMEA 0183** sentences from a GPS sensor via a serial port, parses the data to extract positioning information (GGA and RMC sentences), and maps the coordinates onto a georeferenced satellite image of the **ENSTA Bretagne** campus.



## ⚙️ How it Works

### 1. Data Acquisition (`acquisition.py`)
Connects to a GPS receiver via `pySerial` (configured for COM7, 4800 baud). It captures the raw bitstream, filters NMEA sentences beginning with `$`, and logs them into `gps_data_nmea.txt`.

### 2. Sentence Parsing (`traitement.py`)
Utilizes the `pynmea2` library to decode:
* **GGA Sentences:** Extracted for altitude and fix quality.
* **RMC Sentences:** Extracted for latitude, longitude, and ground speed.
The script includes error handling for `ParseError` to ensure robust processing of noisy serial data.

### 3. Geospatial Visualization (`affichage.py`)
* **Rasterio Integration:** Loads a georeferenced satellite view of the campus.
* **Coordinate Transformation:** Uses the image's affine transform matrix to convert geographic coordinates (Decimal Degrees) into pixel coordinates (x, y).
* **Mapping:** Overlays the receiver's real-time or logged position on the map using `matplotlib`.

## 🛠 Tech Stack
* **Communication:** `pySerial`
* **Parsing:** `pynmea2`
* **Geospatial Analysis:** `rasterio`, `numpy`
* **Visualization:** `matplotlib`

## 🚀 Quick Start

1. **Hardware:** Connect your GPS sensor to your computer.
2. **Install Dependencies:**
Bash
   pip install pyserial pynmea2 rasterio numpy matplotlib
Data Acquisition:

Bash
python acquisition.py
Visualization: Ensure ensta_2015.jpg and gps_data_nmea.txt are in the root directory, then:

Bash
python affichage.py

## 📁 Repository Structure
src/acquisition.py: Serial communication and raw data logging.

src/traitement.py: NMEA parsing logic.

src/affichage.py: Image processing and mapping.

data/gps_data_nmea.txt: Sample raw NMEA log file.

docs/Report_GNSS.pdf: Full technical project report.

## 👥 Authors
Antoine BERTRAND, Samy-William AYYADA, Julien STRUILLOU & Baptiste GUIVARCHE

Academic Context: Developed in 2023 at ENSTA Bretagne.
