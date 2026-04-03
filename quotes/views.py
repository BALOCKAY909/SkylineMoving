from django.shortcuts import render
from .forms import QuoteRequestForm
from django.core.mail import send_mail

# Create your views here.

def quote_request(request):
    success = False

    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            subject = 'New Quote Request from Skyline Moving'
            message = (
                f"First Name: {form.cleaned_data['first_name']}\n"
                f"Last Name: {form.cleaned_data['last_name']}\n"
                f"Email: {form.cleaned_data['email']}\n"
                f"Phone: {form.cleaned_data['phone']}\n"
                f"Job Description: {form.cleaned_data['job_description']}\n"
            )
            send_mail(
                subject,
                message,
                'skyline.moving.gp@gmail.com',
                ['skyline.moving.gp@gmail.com'],
                fail_silently=False,
            )
            success = True
            form = QuoteRequestForm()
    else:
        form = QuoteRequestForm()

    return render(request, 'quotes/quote_form.html', {
        'form': form,
        'success': success,
    })

def thank_you(request):
    return render(request, 'quotes/thank_you.html')

def services(request):
    return render(request, 'quotes/services.html')

def areas_served(request):
    return render(request, 'quotes/areas_served.html')
