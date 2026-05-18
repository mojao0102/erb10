from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.choices import district_choices, room_num_choices, room_type_choices


# Create your views here.
def index(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')[:3]
    #districts = Listing.objects.values('district').distinct().order_by('district')
    context = {"listings" : listings, 
               "districts" : district_choices, 
               "room_choices" : room_type_choices,
               "room_num_choices" : room_num_choices,}
    return render(request, "pages/index.html", context)

def about(request):
    return render(request, "pages/about.html")
