from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from shareRes.models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
# Create your views here.
def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']
    restaurant = []
    for checked_res_ld in checked_res_list:
        restaurant.append(Restaurant.objects.get(id=checked_res_ld))
    content = {'inputContent' : inputContent ,
               'restaurant' : restaurant}
    msg_html = render_to_string('sendEmail/email_format.html',content)

    msg = EmailMessage(subject= inputTitle, body=msg_html,
                       from_email='xmdnlxl0227@gmail.com',
                       bcc=inputReceiver.split(','))
    msg.content_subtype = 'html'
    msg.send()

    return  HttpResponseRedirect(reverse('index'))