# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from send_sms import send
# Create your views here.

# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def post(self, request, **kwargs):
        number = request.POST['contact']
        print(number)
        message = request.POST['text']
        print(message)
        send(number, message)
        #message = request.POST['text']
        return render(request, 'index.html', context=None)

    # def post(self, request, **kwargs):
    #     message = request.POST['text']
    #     print(message)
    #     return render(request, 'index.html', context=None)

    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"
