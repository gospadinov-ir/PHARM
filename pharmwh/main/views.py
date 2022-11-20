from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductsForm

def index(request):
    products = Products.objects.order_by('-id')
    return render(request, 'main/index.html', {'title':'Главая страница сайта', 'products': products})


def about(request):
    return render(request, 'main/about.html')

def management(request):
    error = ''
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Недопустимое значение'


    form = ProductsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/management.html', context)
