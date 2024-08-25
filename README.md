# realtime-weather-app
A simple and intuitive Python-based weather forecast application built using Tkinter. This app allows users to select a city from a predefined list and receive real-time weather updates, including the current climate and temperature.

Features
Real-time Weather Data: Fetches current weather information using the OpenWeatherMap API.
User-Friendly Interface: Designed with Tkinter for a clean and easy-to-use interface.
Wide City Selection: Choose from a list of major cities across India.
Instant Weather Updates: Displays weather conditions and temperature at the click of a button.
Installation
Follow these steps to install and run the Gaurav Weather Forecast App on your local machine:

Clone the Repository:

bash
Copy code
git clone https://github.com/gauravkumarphogat/gaurav-weather-app.git
Navigate to the Project Directory:

bash
Copy code
cd gaurav-weather-app
Install the Required Dependencies: Ensure you have requests installed. If not, you can install it via pip:

bash
Copy code
pip install requests
Run the Application:

bash
Copy code
python app.py
Usage
Launch the application.
Select your city from the dropdown list.
Click the "Done" button to retrieve the latest weather information.
The app will display the current weather climate and temperature in Celsius.
Code Overview
data_get(): This function fetches weather data from the OpenWeatherMap API and updates the labels with the current climate and temperature.
Tkinter Widgets:
Combobox: For selecting the city.
Label: For displaying the app title, weather description, and temperature.
Button: To trigger the data retrieval process.
Requirements
Python 3.x
Tkinter (comes pre-installed with Python)
Requests library (pip install requests)
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
