from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
r1 = [
    {'email':'abc@gmail.com','name':'Srinivasa Nilayam'},
    {'email':'xyz@gmail.com','name':'Ayyappa nilayam'},
]

def home(request):
    context={'rooms':r1}
    return render(request,'home.html',context)
def rooms(request):
    context={'rooms':r1}
    return render(request,'rooms.html',context)
def room(request,pk):
    room = None
    for i in r1:
        if(i['email'] == str(pk)):
            room = i
    context ={'rooms':room}
    return render(request,'room.html',context)
    
