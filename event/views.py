from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Event

import loremipsum as lorem
import names
import os
import random

# Integration with Social Media
from datetime import date
from django.conf import settings
from django.core.mail import send_mail
from multiprocessing import Process
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from twilio.rest import Client

import requests
import smtplib
import threading
import time


# Variables Here
timerSMS = False
timerEmail = False


# Views Here
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.objects.order_by('date_time')


class DisplayView(generic.DetailView):
    template_name = 'display.html'
    context_object_name = 'event'

    def get_queryset(self):
        return Event.objects


class EventNew(generic.CreateView):
    model = Event
    fields = [
        'reporter_last', 'reporter_first',
        'phone_number', 'postal_code',
        'add_desc', 'assist_type',
    ]
    success_url = reverse_lazy('event:index')
    template_name_suffix = '_new'

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = reverse_lazy('event:index')
            return HttpResponseRedirect(url)
        else:
            return super(EventNew, self).post(request, *args, **kwargs)


class EventUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Event
    fields = [
        'reporter_last', 'reporter_first',
        'phone_number', 'postal_code',
        'add_desc', 'assist_type',
    ]
    template_name_suffix = '_edit'

    def get_success_url(self, **kwargs):
        id = self.kwargs['pk']
        url = reverse_lazy('event:display', kwargs={'pk': id})
        return url

    def post(self, request, *args, **kwargs):
        if "back" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(EventUpdate, self).post(request, *args, **kwargs)


class EventDelete(LoginRequiredMixin, generic.DeleteView):
    model = Event
    success_url = reverse_lazy('event:index')
    template_name_suffix = '_delete'

    def post(self, request, *args, **kwargs):
        if "back" in request.POST:
            id = self.kwargs['pk']
            url = reverse_lazy('event:display', kwargs={'pk': id})
            return HttpResponseRedirect(url)
        else:
            return super(EventDelete, self).post(request, *args, **kwargs)


# Generate Random Data
def gen_random_number():
    foo1 = ['6', '8', '9']
    firstDigit = str(random.choice(foo1))
    foo2 = random.randint(1000000, 9999999)
    remainDigit = str(foo2)
    return firstDigit + remainDigit


def valid_postal():
    postal_array = []
    cur_path = os.getcwd()
    file_path = os.path.join(cur_path, 'event', 'generatedata', 'postal.txt')
    with open(file_path, 'r') as file:
        for line in file:
            postal_array.append(line)

    postal = random.choice(postal_array)
    return str(postal).strip()


def gen_assist_type():
    foo = ['A', 'B', 'C', 'D']
    assist = str(random.choice(foo))
    return assist


def createRandomEvent(request):
    Event.objects.create(
        reporter_first=names.get_first_name(),
        reporter_last=names.get_last_name(),
        phone_number=gen_random_number(),
        postal_code=valid_postal(),
        add_desc=lorem.get_sentence(True),
        assist_type=gen_assist_type()
    )
    return render(request, 'gen.html')


# Social Integration
def sendEmail():
    global timerEmail
    threading.Timer(1800, sendEmail).start()
    if (timerEmail):
        points = []
        data = Event.objects.all()
        for point in data:
            points.append(point)
        msg = ''
        for point in points:
            msg = msg + 'Event Name: ' + point.title + '\n Reporter Name: '\
                  + point.reporter_first + '\n Phone Num: ' + point.phone_number + \
                  '\n Postal Code: ' + point.postal_code + '\n Emergency: ' + \
                  point.assist_type + '\n\n'
        send_mail(
            'Subject here',
            msg,
            'ssadxyzssad@gmail.com',
            ['ssadxyzssad@gmail.com'],
            fail_silently=False,)
    timerEmail = True

sendEmail()


# def sendSMS():
#     global timerSMS
#     threading.Timer(300, sendSMS).start()
#     # Your Account Sid and Auth Token from twilio.com/console
#     if (timerSMS):
#         account_sid = 'AC88a195561b25d7a3d90eb51168c0a186'
#         auth_token = 'c5578c0ba3bb19fa20c8bfde614463e6'
#         client = Client(account_sid, auth_token)
#         phonenumbers=["+6597716052"]
#         points = [];
#         data = Event.objects.all()
#         for point in data:
#             points.append(point)
#         msg= ''
#         for point in points:
#             msg = msg + 'Event Name: ' + point.evt_name + '\n Reporter Name: ' \
#                   + point.reporter_name + '\n Phone Num: ' + point.phone_num + \
#                 '\n Postal Code: ' + point.postal_code + '\n Emergency: ' + \
#                 point.emergency_type + '\n\n'
#         message = client.messages.create(
#             body =msg,
#             from_='+12243343676',
#             to = "+6597716052",
#         )
#     timerSMS=True
# sendSMS()
#
#
# class BotHandler:
#     def __init__(self, token):
#             self.token = token
#             self.api_url = "https://api.telegram.org/bot{}/".format(token)
#     #url = "https://api.telegram.org/bot<token>/"
#     def get_updates(self, offset=0, timeout=30):
#         method = 'getUpdates'
#         params = {'timeout': timeout, 'offset': offset}
#         resp = requests.get(self.api_url + method, params)
#         result_json = resp.json()['result']
#         return result_json
#     def send_message(self, chat_id, text):
#         params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
#         method = 'sendMessage'
#         resp = requests.post(self.api_url + method, params)
#         return resp
#     def get_first_update(self):
#         get_result = self.get_updates()
#         if len(get_result) > 0:
#             last_update = get_result[0]
#         else:
#             last_update = None
#         return last_update
#     def updateUser(bot,job):
#         job.context.message.reply_text("Incident occurred at ")
#     def time(bot, update, job_queue):
#         job = job_queue.run_repeating(bot.updateUser, 5, context=update)
# token = '735655596:AAGGD0q6cpSXz2Bh4q5hTJLlX5-8-BL9KgM' #Token of your bot
# bot = BotHandler(token) #Your bot's name
# def sendTelegram():
#     new_offset = 0
#     updater = Updater(token)
#     def callback_user(bot, job):
#         points = [];
#         data = Event.objects.all()
#         for point in data:
#             points.append(point)
#         msg =''
#         for point in points:
#             msg = msg + 'Event Name: ' + point.evt_name + '\n Reporter Name: ' \
#                   + point.reporter_name + '\n Phone Num: ' + point.phone_num + \
#                   '\n Postal Code: ' + point.postal_code + '\n Emergency: ' + \
#                   point.emergency_type + '\n\n'
#         bot.send_message(chat_id=622969283, text=msg)
#     jobQueue = updater.job_queue
#     jobQueue.start()
#     jobQueue.run_repeating(callback_user, interval=20, first=5)
# sendTelegram()
