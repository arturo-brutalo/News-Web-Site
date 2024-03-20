from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect
from .forms import EmailForm
import threading
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from Client.models import News
def send(theme, message, mail):
    try:
        send_mail(theme, message, settings.EMAIL_HOST_USER, mail)
    except Exception as e:
        print(e)

class EmailView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = EmailForm()
        return render(request, 'Email.html', context={"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = EmailForm(request.POST)
        if form.is_valid:
            print(request.POST)
            threading.Thread(target=send, args=('You have signed in News Web-site', f"Имя:{request.POST.get('name')} Почта:{request.POST.get('email_adress')} Сообщение : Soon(never) will be a new update of our web-site, it'll be as soon as i'l get 100 points, if you haven't done anything, just ignore this letter", [request.POST.get('email_adress')])).start()
            return redirect("/log_in")
        else:
            return render(request, 'Email.html', context={"form": form})

class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        if request.user.is_authenticated:
            return render(request, 'main.html', {'news': news})
        else:
            return render(request, 'main_not_logged_in.html', {'news': news})

