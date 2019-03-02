from django.shortcuts import render,  render_to_response
from apps.gallery.models import Gallery
from django.core.mail import send_mail


def home(request):
    gallerys = Gallery.objects
    return render(request, 'home.html', {'gallerys': gallerys})


def page_not_found(request):
    send_mail('Test', 'Test', '892714129@qq.com', ['ranxiaolang@163.com'], html_message=False)
    return render_to_response('404.html')


def page_error(request):
    return render_to_response('500.html')










