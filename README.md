# Gaurav Weather Forecast App

A Python-based weather app built using Tkinter, providing real-time weather updates.

## Features

- **Real-time Weather Data**: Fetches current weather using the OpenWeatherMap API.
- **User-Friendly Interface**: Clean, simple GUI built with Tkinter.
- **Wide City Selection**: Choose from a list of major cities across India.
- **Instant Weather Updates**: Displays climate and temperature at the click of a button.

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/gauravkumarphogat/gaurav-weather-app.git
   ```
   
2. **Navigate to the project directory**:
   ```
   cd gaurav-weather-app
   ```

3. **Install the required dependencies**:
   ```
   pip install requests
   ```

4. **Run the application**:
   ```
   python app.py
   ```

## Usage

1. Launch the application.
2. Select your city from the dropdown list.
3. Click the "Done" button to get the latest weather information.
4. The app will display the current weather condition and temperature in Celsius.

## Code Overview

- **`data_get()` Function**: Fetches weather data from the OpenWeatherMap API and updates the displayed information.
- **Tkinter Widgets**:
  - **Combobox**: For city selection.
  - **Labels**: For displaying the app title, weather information, and temperature.
  - **Button**: To trigger the weather data retrieval.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- Requests library (install via `pip install requests`)

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or bug fixes.

## License

This project is licensed under the MIT License.
