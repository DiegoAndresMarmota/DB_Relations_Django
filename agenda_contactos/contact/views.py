from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def index(request):
    contacts = Contact.objects.filter(name__contains=request.GET.get("search", ""))
    context = {"contacts": contacts}
    return render(request, "contact/index.html", context)


def view(request, id):
    contact = Contact.objects.get(id=id)
    context = {"contact": contact}
    return render(request, "contact/detail.html", context)


def edit(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == "GET":
        form = ContactForm(instance=contact)
        context = {"form": form, "id": id}
        return render(request, "contact/edit.html", context)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        context = {"form": form, "id": id}
        messages.success(request, "El Perfil del contacto se ha actualizado.")
        return render(request, "contact/edit.html", context)
