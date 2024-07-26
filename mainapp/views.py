from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import RegistrationForm
from django.conf import settings
# Create your views here.
def homePage(request):
    return render(request,'index.html')

def headerSliderClassicPage(request):
    return render(request,'index--header-slider-classic.html')

def headerSliderPage(request):
    return render(request,'index--header-slider.html')

def homeClassicPage(request):
    return render(request,'index--home-classic.html')

def selfhostedClassicPage(request):
    return render(request,'index--selfhosted-classic.html')

def selfhostedPage(request):
    return render(request,'index--selfhosted.html')

def youtubeClassicPage(request):
    return render(request,'index--youtube-classic.html')

def youtubePage(request):
    return render(request,'index--youtube.html')

def cloudPage(request):
    return render(request,'cloudcomputing.html')

def course1(request):
    return render(request,'course1.html')

def course2(request):
    return render(request,'course2.html')


def course3(request):
    return render(request,'course3.html')

def course4(request):
    return render(request,'course4.html')

def course5(request):
    return render(request,'course5.html')

def course6(request):
    return render(request,'course6.html')

def course7(request):
    return render(request,'course7.html')


def pasteventsPage(request):
    return render(request,'pastevents.html')

def registration_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')
        state = request.POST.get('state')
        country = request.POST.get('country')
        
        # Save data to the model
        registration = RegistrationForm(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            course=course,
            state=state,
            country=country
        )
        registration.save()  # Save the instance to the database
        
        # Send confirmation email
        send_mail(
            'Registration Successful',
            f'Thank you for registering , {first_name} {last_name}!',
            'your_email@example.com',  # From email
            [email],  # To email
            fail_silently=False,
        )
        
        return redirect('success')  # Redirect to a success page or another view

    return render(request, 'index.html')

def success_page(request):
    return render(request, 'success.html')
