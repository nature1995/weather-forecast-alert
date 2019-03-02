# weather-forecast-alert

<div align="center">
    <a href=""><img src="https://i.loli.net/2019/03/02/5c79e69702a5f.png" width="200" hegiht="200"/></a>
</div>
<br>

## Introduction  
This Django web app can provide weather forecasts with chart display and notifications.

## Features  
- [x] Choose the city to get weather
- [X] Display current weather condition
- [x] Display Forecast as a chart(5 day / 3 hour forecast)
- [x] Set email notifications to notify the user if the temperature is below 45 °F

## Demo
```
http://47.93.251.173/  
```
If you find the online demo do not work, please follow the next part to run the code local.

## Run the code local:  
1. Clone this repository:
```
git clone https://github.com/nature1995/weather-forecast-alert.git
```
2. Enter into `weather-forecast-alert`  folder, set up virtual environment with **python 3.6** and install packages.
```
 cd weather-forecast-aler
 pip3 install -r requirements.txt
```
3. Run server on your own computer:
```
python manage.py runserver 0.0.0.0:8000
```
4. Access though browser
```
http://127.0.0.1:8000
http://0.0.0.0:8000
```
**Notice:**

OWM_API_KEY: `/weather-forecast-alert/apps/weather/views.py`

GOOGLE_MAP_KEY: `/weather-forecast-alert/apps/weather/views.py`

## Author  
[nature1995](https://github.com/nature1995) | Ziran Gong

