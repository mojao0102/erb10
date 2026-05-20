from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from listings.models import Listing
from contacts.models import Contact

# Create your views here.
def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request,"User exist already")
                return redirect("accounts:register")    

            if User.objects.filter(email=email.lower()).exists():
                messages.error(request,"Email exist already")
                return redirect("accounts:register")

            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request, "User created")
            return redirect("accounts:login")
        else:
            messages.error(request, "Password not match")
            return redirect("accounts:register")
        
    else: #GET
        return render(request, "accounts/register.html")

def login(request):

    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            #messages.success(request, "Login successful")
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("accounts:login")

    return render(request, "accounts/login.html")

def logout(request):   

    if request.method == "POST":      
        auth.logout(request)
        messages.success(request, "Logout successful")
        return redirect("accounts:login")
    
    return render(request, "accounts/logout.html")

def dashboard(request):  
    contacts = Contact.objects.all().order_by("-contact_date")
    context = {"contacts" : contacts}
    return render(request, "accounts/dashboard.html", context)
