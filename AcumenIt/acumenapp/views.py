from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
import pyqrcode as pyq
from django.urls import reverse
from .models import Profile,Event,EventDetails,Organizer,Team
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def home(request):
    user = request.user
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'acumenapp/home.html', {'user': user})
    else:
        return render(request, 'acumenapp/home.html')


def events(request):
    return render(request,"acumenapp/events.html")

def map3d(request):
    return render(request,"acumenapp/map3D.html")

def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        user1 = User.objects.get(username=user)
        pro = Profile.objects.get(user=user1)
        ee = EventDetails.objects.filter(qr_code=pro)
        eelist = []
        evlist = []
        for eventdet in ee:
            eelist.append(eventdet)
            ev = Event.objects.get(event_id=eventdet.event_id)
            evlist.append(ev)
            print(ev.event_name)
        for shi in evlist:
            print(shi)
        return render(request, 'acumenapp/dashboard.html', {'pro': pro, 'ee': eelist, 'ev': evlist})
    else:
        return redirect(reverse('home'))
    pass
def register(request):
    if request.method == 'POST':
        emailid = request.POST.get("email")
        password = request.POST.get('password')
        mobile_number = request.POST.get('mobile')
        user = User.objects.create_user(username=emailid, email=emailid, password=password)
        print(user)
        user.is_staff = True
        user.save()
        qrcode = 'ACUMENIT' + get_random_string(5).lower()
        sample = pyq.create(qrcode)
        sample.png('acumenapp/static/img/' + emailid[:-10] + '.png', scale=10)
        mail_subject = 'Activate your AcumenIT account.'
        message = 'Your Qr is:'
        email = EmailMessage(
            mail_subject, message, to=[emailid]
        )
        email.attach_file('acumenapp/static/img/' + emailid[:-10] + ".png")
        email.send()
        profile = Profile(user=user, phone_number=mobile_number, qr_code=emailid[:-10])
        profile.save()
        login(request, user)
        return redirect(reverse("dashboard"))
        pass
    pass

#login Page
def registration(request):
    return render(request,"acumenapp/registration.html")

def sponsers(request):
    return render(request,"acumenapp/sponsers.html")

def team(request):
    return render(request,"acumenapp/team.html")

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

def login_view(request):
    if request.method == 'POST':
        # user = User.objects.create_user(**request.POST)
        #print(request.POST['email'],request.POST.get('password'))
        mail=request.POST.get('email')
        pw=request.POST.get('password')
        user = authenticate(username=mail, password=pw)
        print(user)
        if user is not None:
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            return HttpResponse("Received")

def event_reg(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "GET":
            event = request.GET.get('event')
            ee=Event.objects.get(event_id=event)
            print(event,ee.event_cost)
            user1 = User.objects.get(username=user)
            print(user1)
            pro = Profile.objects.get(user=user1)
            pro.cost=pro.cost+ee.event_cost
            pro.save()
            print(pro.pk)
            ed=EventDetails(event_id=ee,team_id='none',qr_code=pro,status_choice='WAITING')
            ed.save()
            print(request.user.username)
            return HttpResponse("success")
    else:
        return redirect(reverse('home'))