from django.shortcuts import render, redirect

# views here.
def contact_page(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')

    if request.method == 'GET' and request.GET.get('name'):
        name = request.GET.get('name')
        email = request.GET.get('email')
        subject = request.GET.get('subject')
        message = request.GET.get('message')
        # print(f"Contact form submitted: name={name}, email={email}, subject={subject}, message={message}") 
        # to view the response in the terminal from the form submission 

        person.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        return redirect('contact')

    return render(request, 'contact/contact.html')

from .models import person

def view_responses(request):
    """Display all contact form responses"""
    responses = person.objects.all().order_by('-id')
    return render(request, 'response.html', {'responses': responses})


