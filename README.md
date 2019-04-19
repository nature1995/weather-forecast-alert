# weather-forecast-alert

<div align="center">
    <a href=""><img src="https://i.loli.net/2019/03/02/5c79e69702a5f.png" width="200" hegiht="200"/></a>
</div>

[![Build Status](https://travis-ci.com/nature1995/weather-forecast-alert.svg?token=ihxd9jwdJ367UvYy3j9G&branch=master)](https://travis-ci.com/nature1995/weather-forecast-alert)

## Introduction  
This Django web app can provide weather forecasts with chart display and notifications.

## Features  
- [x] Choose the city to get weather
- [X] Display current weather condition
- [X] Display current city map
- [x] Display Forecast as a chart(5 day / 3 hour forecast)
- [x] Set email notifications to notify the user if the temperature is below 45 °F

## Demo

https://www.ranxiaolang.com/weather

If you find the online demo do not work, please follow the next part to run the code local.

## Run the code local:  
1. Clone this repository:
```
git clone https://github.com/nature1995/weather-forecast-alert.git
```
2. Enter into `weather-forecast-alert`  folder, set up virtual environment with **python 3.6** and install packages.
```
 cd weather-forecast-alert
 pip3 install -r requirements.txt
```
3. Update API key

OpenWeatherMap API key:    
OWM_API_KEY: `./weather-forecast-alert/apps/weather/views.py` 

Email key: (See email to find the latest key)  
EMAIL_HOST_PASSWORD: `./weather-forecast-alert/Weather/settings.py`

4. Run server on your own computer:
```
python manage.py runserver 0.0.0.0:8000
```
5. Access though browser
```
http://127.0.0.1:8000
or
http://0.0.0.0:8000
```

## Result
1. Weather forecasts with chart display
<div>
<img src="https://i.loli.net/2019/03/03/5c7ab32ed266a.png" width="250" height="450" alt="Result01.png" title="Result01.png" />
<img src="https://i.loli.net/2019/03/03/5c7ab32ed985c.png" width="250" height="450" alt="Result03.png" title="Result03.png" />
<img src="https://i.loli.net/2019/03/03/5c7ab32ecec0d.png" width="250" height="450" alt="Result02.png" title="Result02.png" />  
</div>

2. Notifications though email
<div>
<img src="https://i.loli.net/2019/03/03/5c7ab32e7e596.png" width="250" height="450" alt="Result04.png" title="Result04.png" />
<img src="https://i.loli.net/2019/03/03/5c7ab32e84970.png" width="250" height="450" alt="Result05.png" title="Result05.png" />
</div>

3. Show figure with Smoothed Line Chart or Histogram
<div>
<img src="https://i.loli.net/2019/03/03/5c7abb9c5b893.png" height="250" alt="Result06.png" title="Result06.png" />
<img src="https://i.loli.net/2019/03/03/5c7abb9c903c2.png" height="250" alt="Result07.png" title="Result07.png" />
</div>

#### Notice:
OpenWeatherMap API key:  
OWM_API_KEY: `./weather-forecast-alert/apps/weather/views.py`

Google Map API key:   
GOOGLE_MAP_KEY: `./weather-forecast-alert/apps/weather/views.py`  

Set your Email:   
Location: `./weather-forecast-alert/Weather/setting.py`  
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465  # Your send port
EMAIL_HOST_USER = 'weather@ranxiaolang.com'
EMAIL_HOST_PASSWORD = 'Your Password'  # Use the dedicate password not your email password
EMAIL_USE_SSL = True  # SSL or TSL depend on email provider
```

## Author  
[nature1995](https://github.com/nature1995) | Ziran Gong

