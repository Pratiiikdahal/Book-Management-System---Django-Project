from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def add_author(request):
    form=add_author_form()
    if request.method=='POST':
        form=add_author_form(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
        else:
            form=add_author_form()
    context={
        'form':form
    }
    return render(request,'authorcreate.html',context=context)

def author_display(request):
    data=Author.objects.all()
    context={
        'authors':data
    }
    return render(request,'authorlist.html',context=context)
