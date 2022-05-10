import email
from sre_constants import SUCCESS
from ssl import Purpose
from unicodedata import name
from django.shortcuts import render, HttpResponse
from datetime  import datetime
from App.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # messages.success(request,"messi is rth")

    return render(request,'index.html')
    

    # def index(request):
    #     return render(request,'index.html')
# def about(request):
    
#     return render(request,'about.html')
# def services(request):
    
#     return render(request,'services.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        purpose= request.POST.get('purpose')
        contact = Contact(name=name,email=email,number=number,purpose=purpose,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Complaint has Been sent')
        
    
    return render(request,'contact.html')
