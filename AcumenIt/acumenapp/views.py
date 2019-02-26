from django.shortcuts import render
from django.core.mail import EmailMessage
import pyqrcode as pyq
from django.contrib.auth.decorators import login_required

# Create your views here.
def email(request):
    return render(request,'acumenapp/email_attch.html')
def snd_mail(request):
    qrcode ='nithish123'
    sample = pyq.create(qrcode)
    sample.png(qrcode + '.png', scale=10)
    mail_subject = 'Activate your AcumenIT account.'
    message='Your Qr is:'
    #message.attach_file("nithish123.png")
    email = EmailMessage(
        mail_subject, message, to=["kannamshivakumar417@gmail.com"]
    )
    email.attach_file('nithish123.png')
    # email.attach(qrcode+'.png',sample.png(qrcode+'.png',scale=6),'image/png')
    # email.attach(sample.name,sample.read)
    #email.attach_file('test.png')
    email.send()
    print(message)
    return render(request,'acumenapp/email_attch.html')
def login(request):
    return render(request,'acumenapp/login.html')
def dashboard(request):
    return render(request,'acumenapp/dashboard.html')
