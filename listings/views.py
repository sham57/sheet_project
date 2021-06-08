from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from listings.models import Listing
from realtors.models import Realtor
from django.shortcuts import get_object_or_404
from .choices import state_choice,bedroom_choice,price_choice
def index(request):
    listings= Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(listings,2)
    page_number=request.GET.get('page')
    page_list=paginator.get_page(page_number)
    context={
    'listings':page_list
    }
    return render(request,'listings/listings.html', context)
def listing(request,listing_id):
    #is_mvp = Realtor.objects.all().filter(is_mvp=True)

    listing=get_object_or_404(Listing, pk=listing_id)
    context={
        'listing':listing,

    }
    return render(request,'listings/listing.html',context)
def search(request):
    query_set=Listing.objects.all().order_by('-list_date')
    #Keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            query_set=query_set.filter(descriptiom__icontains=keywords)
    #City
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            query_set=query_set.filter(city__iexact=city)
    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set=query_set.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            query_set=query_set.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set=query_set.filter(price__lte=price)

    context={
        'state_choice':state_choice,
        'bedroom_choice':bedroom_choice,
        'price_choice':price_choice,
        'listing':query_set,
        'values':request.GET,
    }
    return render(request,'listings/search.html',context)
