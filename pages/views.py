from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.choices import district_choices, room_num_choices, room_type_choices
from doctors.models import Doctor


# Create your views here.
def index(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')[:3]
    #districts = Listing.objects.values('district').distinct().order_by('district')
    context = {"listings" : listings, 
            "districts" : district_choices, 
            "room_type_choices" : room_type_choices,
            "room_num_choices" : room_num_choices,}
    return render(request, "pages/index.html", context)

def about(request):
    doctors = Doctor.objects.order_by('-hire_date')[:3]
    mvp_doctors = Doctor.objects.all().filter(is_mvp=True)
    context = {"doctors" : doctors, "mvp_doctors" : mvp_doctors}

    print(mvp_doctors)

    return render(request, "pages/about.html", context)
