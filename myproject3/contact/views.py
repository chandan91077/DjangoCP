from django.shortcuts import render

# Create your views here.
def contact_page(request):
    return render(request, 'contact/contact.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import person

# def contact_form(request):
#     """Handle contact form submission"""
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
        
#         # Save to database
#         person.objects.create(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message
#         )
#         messages.success(request, 'Message sent successfully!')
#         return redirect('contact_form')
    
#     return render(request, 'contact/form.html')

def view_responses(request):
    """Display all contact form responses"""
    responses = person.objects.all().order_by('-id')
    return render(request, 'response.html', {'responses': responses})