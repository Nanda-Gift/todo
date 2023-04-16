from django.shortcuts import render,redirect
from .models import todolist

# Create your views here.


def todoviews(request):
    todol = todolist.objects.all()
    return render(request, "home.html", {"items":todol})

def entry(request):
    if request.method == 'POST':
        text = request.POST['text']
        email = request.POST['email']
        new=todolist(text=text,email=email)
        new.save()
         
                
        return redirect('todoviews')
    return render(request,'form.html')

def email(request):
    todol = todolist.objects.all()
    return render(request, 'email.html',{"gives":todol})

def delete(request,id):

    new=todolist.objects.get(id=id)
    new.delete()
    return redirect('todoviews')

def search_club(request):
    if request.method == 'POST':
        searched= request.POST['searched']
        todolists=todolist.objects.all()
        

        return render(request,'search_club.html',{'searched':searched,'todolists':todolists})   
    else:
        return render(request,'search_club.html') 