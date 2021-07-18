from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login as dlogin , logout
from django.contrib.auth.models import User
import razorpay
from djangopay.settings import ROZARPAY_API_KEY,ROZARPAY_SECRET_KEY
from django.views.decorators.csrf import csrf_exempt

client = razorpay.Client(auth=(ROZARPAY_API_KEY, ROZARPAY_SECRET_KEY))

def index(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        amount = amount+'00'
        if amount == '00':
            messages.error(request,  "Enter the amount first then proceed")
            return redirect('/')
        print(amount)
        client = razorpay.Client(
            auth=(ROZARPAY_API_KEY,ROZARPAY_SECRET_KEY))

        order = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
        
        order_id = order['id']
        params = {'amount': amount,'api_key':ROZARPAY_API_KEY,'order_id': order_id}
        return render(request, 'index.html',params)
    return render(request, 'index.html')    

@csrf_exempt
def success(request):
    return render(request, "success.html")


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
        contact = Contact( name = name, email = email, phone = phone, desc = desc)
        contact.save()
        done=True
        return render(request, 'contact.html', {'done':done})
    return render(request,"contact.html")


def handlesignup(request):
    if request.method =="POST":
        # Get the post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        
        pass1 = request.POST['spassword1']
        pass2 = request.POST['spassword2']
        
        username = fname+" "+lname
        error = False
        # check for errorneous input
        if len(username)<10:
            error = True
            
        if pass1!= pass2:
            error = True
            
        
        if error == True:
            messages.error(request, "Invalid credentials")
            return redirect('/')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request,  "Your account created successfully")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")


def handlelogin(request): 
    if request.method =="POST":
        # Get the post parameters
        name = request.POST['llname']
        pass1 = request.POST['lpassword1']
        user = authenticate(username = name, password = pass1)
        
        if user is not None:
            dlogin(request, user)
            messages.success(request, "You are loggedin successfully")
            return redirect('/')
        else:         
            messages.error(request, "invalid credentials")
            return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')   














 
