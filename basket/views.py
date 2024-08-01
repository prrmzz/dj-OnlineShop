# from django.shortcuts import render
# from django.views.decorators.http import require_POST
# from .forms import AddToBasketForms
from django.http import HttpResponse
from django.template import loader
# from aproduct.models import Product
from django.shortcuts import render

# def addtobasket(request):
#     if request.method == 'POST':
#         form = AddToBasketForms(request.POST)
#         if form.is_valid():
#             proudct = form.cleaned_data['product']
#             quantity = form.cleaned_data['quantity']
#     else:
#         form = AddToBasketForms()
#
#     return render(request, 'products/product_list.html', {'form': form})

def parham(request):
    template = loader.get_template('basket/basket_list.html')
    return HttpResponse(template.render())

def productlist(request):
    products = Product.objects.filter(title__contains='IPhone')
    contexts = {
        'productz': products,
    }
    return render(request, 'products/product_list.html', context=contexts)

def iphone13(request):
    product13 = Product.objects.filter(title__startswith='IP').filter(title__endswith='13')
    contextss = {
        'iphone13': product13
    }
    return render(request, 'basket/iphone13.html', context=contextss)