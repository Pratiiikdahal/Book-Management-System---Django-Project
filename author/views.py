from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import *
from .models import *
# Create your views here.

#Create operation of Author 
def add_author(request):
    form=add_author_form()
    if request.method=='POST':
        form=add_author_form(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('display-author')
        else:
            form=add_author_form()
    context={
        'form':form
    }
    return render(request,'authorcreate.html',context=context)

#display operation of the Author
def author_display(request):
    data=Author.objects.all()
    context={
        'authors':data
    }
    return render(request,'authorlist.html',context=context)

# Update operation of the Author
def update_author(request,id):
    update_data=Author.objects.get(id=id)
    if request.method=='POST':
        form=add_author_form(request.POST,request.FILES,instance=update_data)
        if form.is_valid():
            form.save()
            return redirect('display-author')
    else:
        form=add_author_form(instance=update_data)
    context={
        'updated_author':form
    }
    return render(request,'authorupdate.html',context=context)

def delete_author(request,id):
    data_to_delete=get_object_or_404(Author,id=id)
    data_to_delete.delete()
    return redirect('display-author')
    
