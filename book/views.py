from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import *
# Create your views here.

def add_book(request):
    form=addbook_form()
    if request.method=='POST':
        form=addbook_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=addbook_form()
    context={
        'form':form
    }
    return render(request,'bookcreate.html',context=context)

def show_book(request):
    # show_book=Book.objects.all()
    show_book = Book.objects.prefetch_related('author') # yes, it does run the objects.all() query and also fetches the author too , specially used in the many to many filed.
    the_messsage='Inside Book/View'
    context={
        'message':the_messsage,
        'book_list':show_book,
    }
    for i in context['book_list']:
        print(i)
    # print(context)
    return render(request,'showbooks.html',context=context)

def display_book(request):
    all_books=Book.objects.all()
    my_message='welcome to BMS'
    context={
        'display_book':all_books,
        'message':my_message,
    }
    return render(request,'home.html',context=context)


def update_books(request,id):
    book=Book.objects.get(id=id)
    
    if request.method=='POST':
        form=addbook_form(request.POST,request.FILES,instance=book)
        form.save()
        return redirect('show-book')
    else:
        form=addbook_form(instance=book)
    context={
            'update_form':form
    }
    return render(request,'update.html',context=context)


def delete_books(request,id):
    to_be_deleted=get_object_or_404(Book,id=id)
    to_be_deleted.delete()
    return redirect(request,'show-book')


def add_publication(request):
    form=addpublication_form()
    if request.method=='POST':
        form=addpublication_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display-publication')
    else:
        form=addpublication_form()
    context={
        'form':form
    }
    return render(request,'publicationcreate.html',context=context)
    
def display_publication(request):
    all_publication=Publication.objects.filter(isActive=True)
    context={
        'display_publication':all_publication,
    }
    return render(request,'publicationview.html',context=context)

def edit_publication(request,id):
    publication_update=Publication.objects.get(id=id)
    
    if request.method=='POST':
        form=addpublication_form(request.POST,request.FILES,instance=publication_update)
        form.save()
        return redirect('display-publication')
    else:
        form=addpublication_form(instance=publication_update)
    context={
        'update_pub_form':form
    }
    return render(request,'publicationupdate.html',context=context)

def delete_publication(request,id):
    pub_del_obj=Publication.objects.get(id=id)
    pub_del_obj.delete()
    return redirect('display-publication')
