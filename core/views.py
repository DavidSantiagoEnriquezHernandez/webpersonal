from django.shortcuts import render
from .models import Work


def home(request):
    return render(request, "core/home.html"  )


def about(request):
    return render(request, "core/about.html"  )

def portfolio(request):
    return render(request, "core/portfolio.html" )

def road(request):
    works = Work.objects.all()
    return render(request, "core/road.html", {'works' : works} )