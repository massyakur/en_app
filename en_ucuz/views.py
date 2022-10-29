from django.shortcuts import render
from en_bilgisayar.models import Product, All
from en_bilgisayar.filters import ProductFilter
from itertools import chain
from django.core.paginator import Paginator
from django.db.models import Q



def en_ucuz(request):

    q = request.GET.get('q')
    
    if q:
        multiple_q = Q(Q(item_name__icontains=q) | Q(item_site_name__icontains=q))
        products = Product.objects.filter(multiple_q)

    else:
        products = Product.objects.all()
    
    filtered_products = ProductFilter(request.GET, queryset=products)

    others = All.objects.all().order_by('item_price')
    # others = list(chain(All.objects.all(), Product.objects.all()))
    # others = sorted(others, key='item_price')
    
    paginated_filtered_products = Paginator(filtered_products.qs, 10)
    page_number = request.GET.get('page', 1)
    product_page_obj = paginated_filtered_products.get_page(page_number)

    context = {
        'products': filtered_products,
        'products_obj': product_page_obj,
        'others': others,
    }

    return render(request, 'en_ucuz/main.html', context)