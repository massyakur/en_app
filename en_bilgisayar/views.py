from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from .filters import ProductFilter

def home(request):
    products = Product.objects.all()[:12]
    return render(request, 'en_bilgisayar/main.html', {'products': products})

def show_all(request):

    ordering = request.GET.get('ordering', "")
    price = request.GET.get('price', "")
    rating = request.GET.get('rating', "")
    search = request.GET.get('search', "")
    # brand_list = []
    # q = Product.objects.values_list("item_brand").distinct()
    # for e in q:
    #     brand_list += e
    # brand_list.sort()
    # print(brand_list)

    if search:
        products = Product.objects.filter(item_name__icontains = search)
    else:
        all_products = Product.objects.all()
    if ordering:
        products = products.order_by(ordering)

    products = ProductFilter(request.GET, queryset=Product.objects.all())

    p = Paginator(products, 15) #
    page = request.GET.get('page', 1)
    #products = p.get_page(page)
    page_range = p.get_elided_page_range(number=page)
    # print(page_range)
    context = {
        'products': products, 
        'page_range': page_range, 
        # 'brand_list': brand_list,
    }

    return render(request, 'en_bilgisayar/products.html', context)

def product_detail(request, name):
    product = Product.objects.get(item_name=name)
    # print(product._id)
    n = range(500)
    return render(request, 'en_bilgisayar/product_detail.html', {'product': product, 'n': n})
