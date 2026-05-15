from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator

# Create your views here.
def listings(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 3)  
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    # print("--- 所有物件的完整資料 ---")
    # # print(f"At page: {paged_listings.number}")
    # # for listing in paged_listings:
    # #     data = {k: v for k, v in listing.__dict__.items() if k != '_state'}
    # #     print(data)
    # print("paginator",paginator)
    # print("page",page)
    # print("------------------------")

    context = {"listings": paged_listings}
    return render(request, "listings/listings.html", context)

def listing(request, listing_id):
    return render(request, "listings/listing.html")
