from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
# Create your views here.
def contact(request):
    if request.method == "POST":
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']
        listing_id = request.POST['listing_id']
        listing=request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            has_contacted=Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made enquiry on this proprty')
                return redirect('/listings/'+listing_id)

        contact=Contact(listing_id=listing_id, listing = listing,name=name, email=email,message=message,phone=phone,user_id=user_id)
        contact.save()
        send_mail(
        "Inquiry on Listed Property",
        "Hello, Hope this mail finds you well!!. There is an nequiry for property "+listing+" Please visit admin site for more details.Thank You!!",
        "munakar0813@gmail.com",
        [realtor_email,'ranjitkarsheetala@gmail.com'] ,
        fail_silently = False
        )
        messages.success(request, 'Thank you for inquiry and Realtor will contact soon')
        return redirect('/listings/'+listing_id)
