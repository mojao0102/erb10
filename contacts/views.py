from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):

    if request.method == "POST":
        listing = request.POST["listing"]
        listing_id = request.POST["listing_id"]
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        phone = request.POST["phone"]
        user_id = request.POST["user_id"]
        #user_id = request.user.id if request.user.is_authenticated else 0

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, message=message, phone=phone, user_id=user_id)
        contact.save()
        if contact:
            messages.success(request, "Inquiry sent")
        else:
            messages.error(request, "Fail to sent inquiry")           
        return redirect("listings:listing", listing_id)

    return render(request, "contacts/contact.html")
