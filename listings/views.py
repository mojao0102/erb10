from django.shortcuts import render


# Create your views here.
def listings(request):
    return render(request, "listings/listings.html", {"name":["Oscar", "Tom"], "phone":"11112222"})

def listing(request, listing_id):
    return render(request, "listings/listing.html")

