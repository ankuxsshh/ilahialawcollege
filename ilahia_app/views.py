from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages  

"""
Views module for the Ilahia application.
This module contains the view functions for the Ilahia application.
"""


def index(request):
    """Render the index page."""
    return render(request, "index.html")


def about(request):
    """Render the about page."""
    return render(request, "about.html")


def courses(request):
    """Render the courses page."""
    return render(request, "courses.html")


def gallery(request):
    """Render the gallery page."""
    return render(request, "gallery.html")


def managements(request):
    """Render the managements page."""
    return render(request, "managements.html")


def contactpage(request):
    """Render the contact page."""
    return render(request, "contactpage.html")


def send_message(request):
    """Render the contact page and handle form submission."""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Compose the email
        subject_email = f"New Inquiry : {subject}"
        message_email = f"""
        You have received a new message from {name} 

        Email :
        ({email}).

        Subject : 
        {subject}
        
        Message :
        {message}
        """

        try:
            # Send email
            send_mail(
                subject_email,
                message_email,
                settings.DEFAULT_FROM_EMAIL,
                ['inspirezestdemo@gmail.com'],  # Replace with your client's email address
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully.")
        except Exception as e:
            messages.error(request, f"Failed to send message. Error: {e}")
        
        # Redirect to the contact page (will reload the form with messages)
        return redirect('contactpage')
    
    return render(request, "contactpage.html")


def principal_desk(request):
    """Render the principal's desk page."""
    return render(request, "principal_desk.html")


def chairmans_desk(request):
    """Render the chairman's desk page."""
    return render(request, "chairmans_desk.html")


def admission_process(request):
    """Render the admission process page."""
    return render(request, "admission_process.html")


def fee_structure(request):
    """Render the fee structure page."""
    return render(request, "fee_structure.html")


def vicechairmans_desk(request):
    """Render the vice chairman's desk page."""
    return render(request, "vicechairmans_desk.html")


def administrator_desk(request):
    """Render the administrator's desk page."""
    return render(request, "administrator_desk.html")

def fiveyears(request):
    """Render the course details page."""
    return render(request, "fiveyears.html")


def threeyears(request):
    """Render the course details page."""
    return render(request, "threeyears.html")


def academics(request):
    """Render the academics page."""
    return render(request, "academics.html")


def programs(request):
    """Render the programs page."""
    return render(request, "programs.html")


def facilities(request):
    """Render the facilities page."""
    return render(request, "facilities.html")


def achievements(request):
    """Render the achievements page."""
    return render(request, "achievements.html")


def moot_court_society(request):
    """Render the moot court society page."""
    return render(request, "moot_court_society.html")


def anti_ragging_cell(request):
    """Render the anti-ragging cell page."""
    return render(request, "anti_ragging_cell.html")


def women_cell(request):
    """Render the women cell page."""
    return render(request, "women_cell.html")


def complaint_cell(request):
    """Render the complaint cell page."""
    return render(request, "complaint_cell.html")


def legal_aid_clinic(request):
    """Render the legal aid clinic page."""
    return render(request, "legal_aid_clinic.html")


def statutory(request):
    """Render the legal aid clinic page."""
    return render(request, "statutory.html")
