from django.http import HttpResponse
from django.shortcuts import render
from landingPage.models import ClientCoffe


def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reviews = request.POST.get('reviews')

        cc = ClientCoffe(firstname=fname, email=email, phone=phone, reviews=reviews)
        cc.save()
    return render(request, 'landingPage/index.html')
