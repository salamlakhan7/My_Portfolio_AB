from django.shortcuts import render
from django.http import HttpResponse,HttpRequest



# Create your views here.
def landing_page(request):
    return render(request,'land.html')

def edu_page(request):
    return render(request,'education.html')

def base_nav(request):
    return render(request,'base.html')

def skills_page(request):
    return render(request,'skills.html')

def projects_page(request):
    return render(request,'projects.html')

def experience_page(request):
    return render(request,'experience.html')

def contact_page(request):
    return render(request,'contactus.html')
