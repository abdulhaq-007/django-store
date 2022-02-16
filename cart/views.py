from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Cart
from .forms import OrderForm
from telepot import Bot
bot = Bot("5116496220:AAHhBGJN_9FYTKx7gwHwW4hDFpQ7QFupBmg")
grID = "1060158414"

# Create your views here.

def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create()
        request.session['user_cart_id'] = cart.id
    return cart


def cartView(request):
    cart = cart_init(request)
    return render(request,"cart.html", {"cart":cart})


import json
def addToCart(request):
    # print(request)
    d = request.GET.get('data')
    data = json.loads(d)
    # print(data)
    product_id = data['product_id']
    quantity = data['count']
    cart = cart_init(request)
    for i in cart.products.all():
        print('Bu id', i.product.id)
        print('bu boshqa hisob', i.product)
        if i.product.id == product_id:
            price = i.product.price * 1
            i.quantity += 1
            i.price += price
            cart.total_quantity += 1
            cart.total_price += price
            i.save()
            cart.save()
            return JsonResponse({'success': 200})
        print('bu boshqa', i.quantity)
    # print('bu', cart.products.all())
    cart.add(product_id,quantity)
    status = {
        'default': 202
    }
    if cart:
        status['success'] = 200
    else:
        status['error'] = 400
    return JsonResponse({'success': 200})



def addToCartQty(request):
    d = request.GET.get('data')
    data  = json.loads(d)
    product_id = data['product_id']
    quantity = data['qty']
    cart = cart_init(request)
    for i in cart.products.all():
        if i.product.id == product_id:
            price = i.product.price * quantity
            i.quantity += quantity
            i.price += price
            cart.total_quantity += quantity
            cart.total_price += price
            i.save()
            cart.save()
            return JsonResponse({'success': 200})
    cart.add(product_id,quantity)
    status = {
        'default': 202
    }
    if cart:
        status['success'] = 200
    else:
        status['error'] = 400
    return JsonResponse(status)


def deleteCartItem(request,product_id,qty):
    cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    cart.deleteItem(product_id,qty)
    return redirect('cart:cart')

def removeCartItems(request):
    cart = cart_init(request)
    cart.removeAllItems()
    return redirect('cart:cart')

def checkout(request):
    cart = cart_init(request)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            us = request.user
            f = form.save(commit=False)
            f.products = cart
            f.user = us
            f.save()
            # message = f"""
            #         Xaridor Akkaunti : {f.user.username}\n\
            #         Xaridor Ismi : {f.first_name}\n\
            #         Xaridor Nomeri : {f.phone}\n\
            #         Xaridor Email : {f.email}\n\
            #         Xaridor Manzili : {f.address}\n\
            #         Xaridor Jami Hisob Kitob : ${f.products.total_price}\n
            #         Xaridor Jami Product Miqdori : donada {f.products.total_quantity}\n
            #         """
            # for item in cart.products.all():
            #     print('Bu image url', item.product.image.url)
            #     print('Bu product name', item.product.name)
            #     print('Bu product price', item.product.price)
            #     print('Bu product quantity', item.quantity)
            #     print('Bu product total price', item.price)
            #     message += f"""\n\
            #         Product Nomi : {item.product.name}\n\
            #         Product Narxi : ${item.product.price}\n\
            #         Product Miqdori : {item.quantity}\n\
            #         Product Jami Narxi : ${item.price}\n\
            #     """
            # bot.sendMessage("1060158414", message)
            # bot.sendMessage("1060158414", "Hey Check Your Admin Panel http://127.0.0.1:8000/super/admin/")
            cart = cart_init(request)
            cart.removeAllItems()
            return redirect('/')
    else:
        form = OrderForm()
    return render(request, "checkout.html", {"form": form, 'cart': cart})

