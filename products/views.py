from django.http import HttpResponse
from products.models import Product, Category


def ProductList(request):
    productlist = Product.objects.all()
    return HttpResponse(productlist)


def CategorySelf(request, category_name):
    normalized_category_name = category_name.replace('-', ' ')
    try:
        categoryself = Category.objects.get(name__iexact=normalized_category_name)
        categoryself_products = Product.objects.filter(category_id=categoryself)
        return HttpResponse(categoryself_products)
    except Category.DoesNotExist:
        return HttpResponse("Category not found", status=404)


def ProductSelf(request, product_name, category_name):
    normalized_product_name = product_name.replace('-', ' ')
    normalized_category_name = category_name.replace('-', ' ')
    try:
        productself = Product.objects.get(name__iexact=normalized_product_name)
        categoryself = Category.objects.get(name__iexact=normalized_category_name)
        if productself.category_id == categoryself:
            return HttpResponse(productself)
        else:
            return HttpResponse("Product doesn't exist in this category", status=404)
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)

