from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import district_choices, room_num_choices, room_type_choices
from django.db.models import Q, F

# Create your views here.
def listings(request):
    listings = Listing.objects.filter(is_published = True).order_by("-list_date")
    paginator = Paginator(listings, 3)  
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {"listings": paged_listings}
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, "listings/listing.html", context)


def search(request):
    #Create Qurrey Set
    filtered_listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            filtered_listings = filtered_listings.filter(Q(description__icontains=keywords) | Q(title__icontains=keywords) | Q(doctor__name__icontains=keywords))  

    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            filtered_listings = filtered_listings.filter(district__iexact=district)

    if 'room_type' in request.GET:
        room_type = request.GET['room_type']
        if room_type:
            filtered_listings = filtered_listings.filter(room_type__icontains=room_type)

    if 'room_num' in request.GET:
        room_num = request.GET['room_num']
        if room_num:
            filtered_listings = filtered_listings.filter(rooms__gte=room_num)

    paginator = Paginator(filtered_listings, 3)
    page = request.GET.get('page')
    paged_filtered_listings = paginator.get_page(page)
    context = {    
            "filtered_listings" : paged_filtered_listings,
            "district_choices" : district_choices, 
            "room_num_choices" : room_num_choices, 
            "room_type_choices" : room_type_choices,
            'values' : request.GET,
            }
    print(request.GET)
    return render(request, "listings/search.html", context)