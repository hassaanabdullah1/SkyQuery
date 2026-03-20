#SkyQuery

**SkyQuery** is a high-performance, object-oriented Command Line Interface (CLI) designed to pull real-time meteorological data directly into your terminal. By bridging the gap between raw API data and a clean user dashboard, SkyQuery provides an efficient way to monitor global weather conditions without the bloat of a web browser.

## 🌟 Key Features

* **Geographical Precision:** Integrated Geocoding API allows you to search by city name and select from a list of global matches to ensure coordinate accuracy.
* **Atmospheric Intelligence:** Detailed reporting on temperature (Actual vs. Feels Like), humidity levels, and cloud coverage.
* **Wind Dynamics:** Real-time tracking of wind speeds, degrees, and gusts.
* **Solar Tracking:** Automated UTC-to-Local conversion for precise Sunrise and Sunset timings.
* **Fault-Tolerant Design:** Built-in logic to handle network timeouts, invalid inputs, and API communication errors.

---

## 🛠️ The Engine Under the Hood

SkyQuery is built with a modular architecture to ensure code maintainability:

* **Python 3.x**: The core logic and data processing.
* **Requests Library**: Handles all asynchronous communication with the OpenWeatherMap infrastructure.
* **OOP Architecture**: Uses dedicated classes for Validation, Data Fetching, and UI Rendering.

---

## 🚀 Installation & Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/hassaanabdullah1/SkyQuery.git
cd SkyQuery
```

### 2. Install Dependencies
```bash
pip install requests
```

### 3. Configure API Access
1.  Obtain a free API Key from [OpenWeatherMap](https://openweathermap.org/api).
2.  Open `WeatherApp.py` and input your key into the `API_KEY` variable:
    ```python
    API_KEY = "your_secret_key_here"
    ```

### 4. Launch SkyQuery
```bash
python main.py
```

---

## 📊 Data Points Delivered
| Category | Data Points |
| :--- | :--- |
| **Temperature** | Current Temp, Feels Like, Cloud % |
| **Atmosphere** | Humidity, Visibility (meters) |
| **Wind** | Speed (m/s), Direction (degrees), Gusts |
| **Solar** | Sunrise Time, Sunset Time |

---

## 🗺️ Roadmap
* [ ] **Unit Conversion:** Toggle between Metric, Imperial, and Scientific (Kelvin) units.
* [ ] **Secure Storage:** Implementation of `.env` support for API keys.
* [ ] **Forecast Engine:** Expansion to 5-day / 3-hour forecast intervals.
* [ ] **Export Mode:** Option to save weather reports to a `.txt` or `.json` file.

---

## ⚖️ License
Distributed under the MIT License. See `LICENSE` for more information.

---

### 💡 Final Step for You
To make the app truly feel like **SkyQuery**, update your `show_data` method one last time:

```python
print(f"\n--- 🛰️  SKYQUERY TERMINAL: {self.result.get('name', 'Location')} ---")
```

**Would you like me to draft a `.gitignore` file for you now so your private API key doesn't accidentally get pushed to GitHub?**
