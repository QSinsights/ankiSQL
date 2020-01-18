from django.shortcuts import render, redirect
from .models import ankidb
from .forms import StoreMemories
from django.contrib import messages

def home(request):

    if request.method == 'POST':
        form = StoreMemories(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = ankidb.objects.all()
            messages.success(request, ('New item added..'))
            return render(request, 'index.html', {'all_items':all_items})

    else:
        all_items = ankidb.objects.all()
        return render(request, 'index.html', {'all_items':all_items})

def delete(request, list_id):

    item = ankidb.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item deleted..'))
    return redirect('home')

def Objective1 (request):
    return render(request, 'Ob1.html')

def Objective2 (request):
    return render(request, 'Ob2.html')

def Objective3 (request):
    return render(request, 'Ob3.html')

def Objective4 (request):
    return render(request, 'Ob4.html')

def Objective5 (request):
    return render(request, 'Ob5.html')

def DBFO (request):
        return render(request, 'DBFO.html')
