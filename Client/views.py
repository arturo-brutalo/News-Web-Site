from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect
from .forms import CreateContactForm, LogInForm
import threading
from django.contrib.auth import authenticate, login

class CreateContactView(View):
    def get(self, request:HttpRequest)->HttpResponse:
        form = CreateContactForm()
        return render(request, 'create_contact.html', context={"form":form})
    def post(self, request: HttpRequest) -> HttpResponse:
        form = CreateContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = form.cleaned_data['name']
            user.last_name = form.cleaned_data['surname']
            user.save()
            return redirect("/send_email")
        else:
            return render(request, "create_contact.html", context={"form": form})

class LogInView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if not request.user.is_authenticated:
            form = LogInForm()
            return render(request, "log_in.html", context={"form": form})
        else:
            return HttpResponsePermanentRedirect("/")

    def post(self, request: HttpRequest) -> HttpResponse:
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponsePermanentRedirect("/")
            else:
                return render(request, "log_in.html", context={"form": form})
        else:
            return render(request, "log_in.html", context={"form": form})