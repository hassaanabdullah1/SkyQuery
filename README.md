# 🛰️ SkyQuery Terminal

**SkyQuery** is a robust Python command-line interface (CLI) that provides detailed weather analytics using the **OpenWeatherMap API**. By utilizing geocoding, it ensures precision by allowing users to select the exact city, state, and country they wish to query.

## 🚀 Key Features
* **Smart Geocoding:** Search for a city name and choose from multiple global matches to get the exact location.
* **Comprehensive Metrics:** Tracks temperature, "feels like" values, humidity, visibility, and cloud coverage.
* **Wind Analytics:** Displays speed, direction, and gust data.
* **Solar Tracking:** Converts raw UTC timestamps into readable local sunrise and sunset times.
* **OOP Architecture:** Built with modular classes (`Validate`, `WeatherData`, `SkyQuery`) for clean, maintainable code.

## 🛠️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/hassaanabdullah1/SkyQuery.git
    cd SkyQuery
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key:**
    * Obtain a free API key from [OpenWeatherMap](https://openweathermap.org/api).
    * Create a file named `.env` in the root directory.
    * Add your key to the file:
        ```env
        API_KEY=your_actual_api_key_here
        ```

## 💻 Usage

Launch the application via your terminal:
```bash
python main.py
```

1.  **Search:** Enter the city name (e.g., "London" or "Tokyo").
2.  **Select:** Choose the correct location from the numbered list of results.
3.  **View:** Analyze the formatted weather report.

## 🧮 Technical Details: Conversions

The application performs real-time data processing for human readability:
* **Temperature:** Converted from Kelvin ($K$) to Celsius ($°C$):
    $$T_{(°C)} = T_{(K)} - 273.15$$
* **Timezones:** Raw offsets are converted into standard UTC format (e.g., `UTC+5`).

## 🛡️ Security

Your API key is protected via `python-dotenv`. Ensure that the `.env` file is listed in your `.gitignore` to prevent it from being shared publicly.
