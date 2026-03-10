from django.shortcuts import render
import qrcode
from django.http import HttpResponse
from io import BytesIO


def qr_page(request):
    whatsapp_url = "https://wa.me/27717109741?text=I%20would%20like%20to%20order%20food%20from%20Ekhaya"
    return render(request, "qr.html", {"whatsapp_url": whatsapp_url})


def generate_qr(request):
    whatsapp_url = "https://wa.me/27717109741?text=I%20would%20like%20to%20order%20food%20from%20Ekhaya"
    qr = qrcode.make(whatsapp_url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return HttpResponse(buffer.getvalue(), content_type="image/png")



def home(request):
    return render(request, "home.html")

def menu(request):
    return render(request, "menu.html")


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")