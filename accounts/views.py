from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Successfully loged out")
        return redirect('index')

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
                messages.error(request,'Username already taken ')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=first_name,username=username,last_name=last_name,email=email,password=password)
                    user.save()
                    messages.success(request, 'Succesful registration')
                    return redirect('login')

        else:
            messages.error(request, 'Password did not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def dashboard(request):
    user_contacts = Contact.objects.order_by("-contact_date").filter(user_id=request.user.id)
    context={
    'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Log in Success')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')
