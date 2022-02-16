from django.shortcuts import render, redirect
# from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import Product
from cart.models import Order
from django.core.paginator import Paginator
from .forms import ContactForm
import random
import json

# Create your views here.


class HomeView(ListView, LoginRequiredMixin):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    # queryset = Product.objects.all().select_related("category")[:8]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     product = list(Product.objects.select_related("category").all().values())
    #     random_product = random.sample(product, 3)
    #     context["features"] = random_product
    #     return context

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'product.html'
    

class ShopView(ListView):
    paginate_by = 6
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    queryset = Product.objects.all().select_related("category")

def detail(request, p_id):
    obj = Product.objects.select_related("category").get(id=p_id)
    category = obj.category
    related_product = Product.objects.filter(category=category)
    print(obj)
    context = {
        "object":obj,
        "products": related_product
    }
    return render(request, "detail.html", context)

def tag_shop(request, category_id):
    related_product = Product.objects.filter(category=category_id)
    paginator = Paginator(related_product, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'page_obj': page_obj, 
    }
    return render(request, "shop.html", context)


# def filter(request):
#     d = json.loads(request.GET['data'])
#     min_value = d['min_value']
#     max_value = d['max_value']
#     category_id = d['category_id']
#     data = {}
#     product = list(Product.objects.filter(price__range=(min_value, max_value), category=category_id).values())
#     data['data'] = product
#     print(data)
#     return JsonResponse(data)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})