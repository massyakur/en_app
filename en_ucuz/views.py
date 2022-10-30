from django.shortcuts import render
from en_bilgisayar.models import Product
from en_bilgisayar.filters import ProductFilter
from itertools import chain
from django.core.paginator import Paginator
from django.db.models import Q



def en_ucuz(request):

    q = request.GET.get('q')
    
    if q:
        multiple_q = Q(Q(item_name__icontains=q) | Q(laptops__startswith={'item_site_name': q})) # 
        products = Product.objects.filter(multiple_q)
    else:
        products = Product.objects.all()
    Product.objects.raw
    filtered_products = ProductFilter(request.GET, queryset=products)
    
    # paginated_filtered_products = Paginator(filtered_products.qs, 10)
    # page_number = request.GET.get('page', 1)
    # product_page_obj = paginated_filtered_products.page(page_number)
    # product_page_obj = paginated_filtered_products.get_page(page_number)


    context = {
        'products': filtered_products,
        # 'products_obj': product_page_obj,
    }

    return render(request, 'en_ucuz/main.html', context)

def product_detail(request, name):
    
    product = Product.objects.get(item_name=name)
    
    n = range(500)
    return render(request, 'en_ucuz/detail.html', {'product': product, 'n': n})