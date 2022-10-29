from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from .filters import ProductFilter
from django.db.models import Q

def home(request):
    products = Product.objects.all()[:12]
    return render(request, 'en_bilgisayar/main.html', {'products': products})

def show_all(request):

    # orderby = request.GET.get('orderby', "")
    # price = request.GET.get('price', "")
    # rating = request.GET.get('rating', "")
    q = request.GET.get('q')
    # brand_list = []
    # q = Product.objects.values_list("item_brand").distinct()
    # for e in q:
    #     brand_list += e
    # brand_list.sort()
    # print(brand_list)

    # if 'q' in request.GET:
    if q:
        multiple_q = Q(Q(item_name__icontains=q) | Q(item_site_name__icontains=q))
        products = Product.objects.filter(multiple_q)

    else:
        products = Product.objects.all()
    # if ordering:
    #     products = products.order_by(ordering)

    # print(all_products)
    
    filtered_products = ProductFilter(request.GET, queryset=products)

    # others = All.objects.all()
    # paginated_filtered_products = Paginator(filtered_products.qs, 15)
    # page_number = request.GET.get('page')
    # product_page_obj = paginated_filtered_products.get_page(page_number)
    # if orderby:
    #     filtered_products = filtered_products.qs.order_by(orderby)



    # p = Paginator(filtered_products.qs, 15) #
    # page = request.GET.get('page', 1)
    # products = p.get_page(page)

    # page_range = paginated_filtered_products.get_elided_page_range(number=page_number)

    # print(page_range)

    context = {
        'products': filtered_products,
        # 'others': others,
        # 'p': product_page_obj,
        # 'page_range': page_range, 
        # 'brand_list': brand_list,
    }

    return render(request, 'en_bilgisayar/products.html', context)

def product_detail(request, name):
    
    product = Product.objects.get(item_name=name)
    
    n = range(500)
    return render(request, 'en_bilgisayar/product_detail.html', {'product': product, 'n': n})
