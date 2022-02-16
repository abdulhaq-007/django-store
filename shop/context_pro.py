from .models import *

def view_all(request):
    context = {
        'banners': BannerHeader.objects.all(),
        'categories': Category.objects.all(),
    }
    return context
