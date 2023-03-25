from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from .form import FormContact
from django.contrib import messages

# Create your views here.


def home(request):

    if request.method == "POST":
        formulario = FormContact(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            name = data_form.get('name') 
            phone = data_form['phone'] 
            email = data_form['email'] 
            message = data_form['messege']

            contact = Contact(
                name = name,
                phone = phone,
                email = email,
                message = message
            )

            contact.save()

            messages.success(request, "Gracias por contactarnos pronto nos comunicaremos")

            return redirect('home')

    else:
        formulario = FormContact

    return render(request, 'home.html', {
        'form': formulario
    })

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):

    if request.method == "POST":
        formulario = FormContact(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            name = data_form.get('name') 
            phone = data_form['phone'] 
            email = data_form['email'] 
            message = data_form['messege']

            contact = Contact(
                name = name,
                phone = phone,
                email = email,
                message = message
            )

            contact.save()

            messages.success(request, "Gracias por contactarnos pronto nos comunicaremos")

            return redirect('contact')

    else:
        formulario = FormContact

    return render(request, 'contact.html', {
        'form': formulario
    })

    