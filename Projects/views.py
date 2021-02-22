from django.shortcuts import render
from .models import *
def Home(request):
    projects=Projects.objects.all;
    print(projects);
    return render(request,'home.html',{'projects':projects})
