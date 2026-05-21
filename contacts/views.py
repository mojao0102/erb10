from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# Create your views here.
def contact(request):

    if request.method == "POST":
        
        if request.user.is_authenticated and Contact.objects.filter(user_id=request.user.id, listing_id = request.POST["listing_id"]).exists():
            messages.error(request, "you has sent inquiry to this clinic before")           
            return redirect("listings:listing", request.POST["listing_id"])
        else:
            listing = request.POST["listing"]
            listing_id = request.POST["listing_id"]
            name = request.POST["name"]
            email = request.POST["email"]
            message = request.POST["message"]
            phone = request.POST["phone"]
            user_id = request.user.id if request.user.is_authenticated else 0
            doctor_email = request.POST["doctor_email"]
            #user_id = request.POST["user_id"]

            contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, message=message, phone=phone, user_id=user_id)
            contact.save()

            '''#Send email to doctor
            send_mail(
                "Clinic Inquiry",
                message,
                "iamos0102@gmail.com",
                [doctor_email],
                fail_silently=False
            )'''

            if contact:
                messages.success(request, "Inquiry sent")
            else:
                messages.error(request, "Fail to sent inquiry")   

            return redirect("listings:listing", listing_id)

    return render(request, "contacts/contact.html")

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect("accounts:dashboard")

def edit_contact(request, contact_id):  
    return redirect("accounts:dashboard")