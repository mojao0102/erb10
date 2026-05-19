from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
                print("User exist already")
                return redirect(request, "accounts:register")    
            else:
                if User.objects.filter(email=email).exists():
                    print("Email exist already")
                    return redirect(request, "accounts:register")
                else:       
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    user.save()
                    print("User created")

        else:
            print("Password not match")
            return redirect(request, "accounts:register")
    else:
        return render(request, "accounts/register.html")

def login(request):

    return render(request, "accounts/login.html")

def logout(request):
    
    return render(request, "accounts/logout.html")
