from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm


def home_page(request):
    context = {
        'title': 'Hello Word!',
        'content': 'Welcome to the homepage.'
    }
    return render(request, 'home.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': 'Welcome to the contact page.',
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        messages.success(request, 'Ok, action is right')
        return render(request, 'contact.html', context)
    else:
        messages.error(request, 'Please, try again')

    return render(request, 'contact.html', context)



