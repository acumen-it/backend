from django.shortcuts import render
from django.core.mail import EmailMessage
import pyqrcode as pyq
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
# Create your views here.

def login(request):
    #mailid = request.GET.get('email')
    #print(mailid)
    #profiles = [x.email for x in Profile]
    #if mailid not in profiles:
        return render(request,'acumenapp/login.html')
    #else:
     #   return render(request,'acumenapp/dashboard.html')
def dashboard(request):
    if request.method == 'POST':
                emailid = request.POST.get('email')
                username = request.POST.get('userName')
                college = request.POST.get('college')
                roll = request.POST.get('rollNo')
                branch = request.POST.get('branch')
                year = request.POST.get('year')
                phone = request.POST.get('mobileNo')
                print(username)
                print(emailid)
                print(phone)
                qrcode = 'ACUMENIT' + get_random_string(5).lower()
                sample = pyq.create(qrcode)
                sample.png(qrcode + '.png', scale=10)
                mail_subject = 'Activate your AcumenIT account.'
                message = 'Your Qr is:'
                email = EmailMessage(
                    mail_subject, message, to=[emailid]
                )
                email.attach_file('VCEIT0wvfm.png')
                email.send()
                print(message)
                obj = Profile(name=username, email=emailid,year =year,
                              college=college, branch=branch, phone_number=phone,
                              roll_number=roll,qr_code=qrcode)
                obj.save()
    return render(request,'acumenapp/dashboard.html',{'name':username,'phone':phone,'roll':roll,'college':college,'year':year})

def home(request):
    return render(request,'acumenapp/home.html')
def events(request):
    return render(request,'acumenapp/events.html')