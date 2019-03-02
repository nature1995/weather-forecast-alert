from django.shortcuts import render
import requests
import random
import datetime
import pytz
from django.core.mail import send_mail

tz = pytz.timezone('America/New_York')
emails = ['892714129@qq.com']
content = ''


def send_email(subject='Weather alert enroll successful<noreply@ranxiaolang.com>', email='892714129@qq.com', content='Weather alert enroll successful'):
    send_mail(subject, content, 'weather@ranxiaolang.com', [email], html_message=False)


def weather(request):
    if request.method == 'POST':
        try:
            ct = request.POST['c'].title()
            now =('http://api.openweathermap.org/data/2.5/weather?q={}&appid=508a300e8b1ea7c704b80a574472ae9f&units=Imperial').format(ct)
            c =('http://api.openweathermap.org/data/2.5/forecast?q={}&appid=508a300e8b1ea7c704b80a574472ae9f&units=Imperial').format(ct)
            cmap = "https://www.google.com/maps/embed/v1/place?key=AIzaSyA7lDyyF5WebJYGR241iCDxl4f7mvZOy4c&q={}".format(ct)
            now_w = requests.get(now)
            w = requests.get(c)
            now_api = now_w.json()
            api = w.json()
            cur_weather = {}
            list = []
            cur_list = []
            cur_weather['name'] = api['city']['name']
            cur_weather['ab'] = now_api['main']['temp']
            cur_weather['dt'] = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
            cur_weather['ds'] = now_api['weather'][0]['description']
            cur_weather['i'] = "http://www.openweathermap.org/img/w/" + now_api['weather'][0]['icon'] + ".png"
            cur_weather['cl'] = now_api['clouds']['all']
            cur_list.append(cur_weather)
            print('Now', now_api)
            print(cur_list)

            for i in range(len(api['list'])):
                weather={}
                c1 = random.randint(1, 99)
                c2 = random.randint(1, 99)
                weather['name'] = api['city']['name']
                weather['ab'] = api['list'][i]['main']['temp']
                weather['dt'] = api['list'][i]['dt_txt']
                weather['ds'] = api['list'][i]['weather'][0]['description']
                weather['i'] = "http://www.openweathermap.org/img/w/"+api['list'][i]['weather'][0]['icon']+".png"
                weather['cl'] = api['list'][i]['clouds']['all']
                list.append(weather)

            content_text = 'Weather alert, lower than 45 °F, current weather is ' + str(cur_weather['ab']) + ' °F'
            if cur_weather['ab'] <= 45.0:
                send_email(subject="Weather alert<noreply@anxiaolang.com>",email= emails[-1],content=content_text)
            col = '#A'+repr(c1)+'f'+repr(c2)
            print('List', list)
            # return render(request,'weather.html',{'a':list,'cur':cur_list, 'color':col,'map':cmap})
            return render(request, 'weather.html', {'a_list': list, 'cur': cur_list, 'color': col, 'map': cmap})
        except KeyError:
            return render(request, 'weather.html', {'e': "Please Enter A valid City Name!!!"})
    elif request.method == 'GET':
        try:
            em = request.GET['em']
            emails.append(em)
            send_email(subject='Weather alert enroll successful<noreply@anxiaolang.com>', email=emails[-1], content='Weather alert enroll successful')
            print(em)
            return render(request, 'weather.html')
        except KeyError:
            return render(request, 'weather.html')
    else:
        pass

    return render(request, 'weather.html')
