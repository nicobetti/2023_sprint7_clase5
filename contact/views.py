from django.shortcuts import render, redirect
from django.urls import reverse
#importamos el modulo donde esta la clase ContactForm
from .forms import ContactForm

# Create your views here.


#Agregamos la vista de contacto que teniamos en la aplicacion de prueba
def contact(request):
    #creamos una isntancia del formulario
    contact_form = ContactForm
    #validamos que ocurrio una peticion POST
    if request.method == "POST":
        #Traemos los datos enviados
        contact_form = contact_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
        #En lugar de renderizar el template de contacto hacemos un redireccionamiento enviando una variable OK
        return redirect(reverse('contact')+"?ok")
    return render(request,'contact/contact.html',{'form': contact_form})