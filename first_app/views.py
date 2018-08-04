from django.shortcuts import render
from .models import LeaveMessage
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

#def index(request):
#   context = {
    
#   }
#   return render(request, 'index.html', context=context)

def index(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['kumar.rohitp098@gmail.com']
            if cc_myself:
                recipients.append(sender)

            total_subject = str(sender) + ': ' + str(subject)

            send_mail(total_subject, message, sender, recipients, fail_silently = False)
            messages.success(request, 'Thank you for contacting me!')
            return render(request, 'index.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})

def successView(request):
    return HttpResponse('Success!')