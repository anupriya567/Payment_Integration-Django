from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contactt, Paymentt
from django.contrib import messages
from django.contrib.auth import authenticate, login as dlogin , logout
from django.contrib.auth.models import User
import razorpay
from djangopay.settings import ROZARPAY_API_KEY,ROZARPAY_SECRET_KEY
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

client = razorpay.Client(auth=(ROZARPAY_API_KEY, ROZARPAY_SECRET_KEY))

def index(request):
    return render(request, 'index.html')   


def donate(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        amount = int(request.POST.get("amount"))*100
        client = razorpay.Client(
            auth=(ROZARPAY_API_KEY,ROZARPAY_SECRET_KEY))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        print(payment)
        pay = Paymentt(name=name, amount=amount, email=email, payment_id = payment['id'])
        pay.save()
        params = {'api_key':ROZARPAY_API_KEY,'payment' : payment}
        return render(request , "donate.html" , params)

    return render(request,'donate.html')



@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key , val in a.items():

            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Paymentt.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
        msg_plain = render_to_string('email.txt')
        msg_html = render_to_string('email.html')

        send_mail("Your donation has been received", msg_plain, settings.EMAIL_HOST_USER,
                 [user.email], html_message = msg_html)
        return render(request,'success.html')

def about(request):
    return render (request,'about.html')


def course(request):
    return render (request,'courses.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        desc = request.POST.get('desc',"")
        contact = Contactt( name = name, email = email, phone = phone, desc = desc)
        contact.save()
        done=True
        return render(request, 'contact.html', {'done':done})
    return render(request,"contact.html")



















 
