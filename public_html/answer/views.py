from django.shortcuts import render
from django_twilio.decorators import twilio_view
import django_twilio
import twilio.twiml

@twilio_view
def hi(request):
    resp = twilio.twiml.Response()
    resp.say('Hello from the cat in sunny Key West')

    resp.play('http://www.the-cat.com/media/Margaritaville.wav')

    resp.say('Goodbye')

    return str(resp)

