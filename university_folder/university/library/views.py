from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def home(request):
    search=request.GET.get('name')

    print(search)
    users = User.objects.all().filter(full_name__contains=search)
    print(users)
    context={"name":users  }

    return render(request,"home.html", context)