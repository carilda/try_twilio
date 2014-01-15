from django.shortcuts import render
from django_twilio.decorators import twilio_view
import django_twilio
import twilio.twiml

@twilio_view
def hi(request):
    resp = twilio.twiml.Response()
    resp.say('Hello from the cat in sunny Key West', voice=twiml.Say.WOMAN)

    resp.play('http://www.the-cat.com/media/Margaritaville.wav')

    resp.say('Goodbye', voice=twiml.Say.WOMAN)

    return str(resp)

