

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
# Create your views here.



def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks babe, your message was sent successfully!")
            return redirect('contact')  # reload the page after submit
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def terms_of_service(request):
    return render(request, 'terms-of-service.html')
def students_life (request):
    return render(request,'students_life.html')
def starter_page(request):
    return render(request, 'starter-page.html')
def privacy(request):
    return render(request, 'privacy.html')
def news_details(request):
    return render(request, 'news-details.html')
def news(request):
    return render(request, 'news.html')
def home(request):
    return render(request, 'home.html')

def faculty_staff(request):
    return render(request, 'faculty-staff.html')
def events(request):
    return render(request, 'events.html')
def event_details(request):
    return render(request,'event-details.html')
def campus_facilities(request):
    return render(request, 'campus-facilities.html')
def alumni(request):
    return render(request, 'alumni.html')
def admissions(request):
    return render(request, 'admissions.html')
def academics(request):
    return render(request, 'academics.html')
# def custom_404_view(request, exception):
#     return render(request, '404.html', status=404)




