from django.shortcuts import render, redirect

# Create your views here.

from . models import ShippingAddress, Order, OrderItem

from django.http import  JsonResponse

from cart.cart import Cart

from django.shortcuts import get_object_or_404

from django.urls import reverse

from django.conf import settings

import json
import requests

api_key = settings.PAYSTACK_TEST_SECRETE_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL

def checkout(request):
    
    # Users with accounts -- Pre-fill the form
    
    cart = Cart(request)
    
    
    if request.user.is_authenticated:
        
        try:
            
            # Authenticated users WITH shipping information
            
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            
            context = {'shipping': shipping_address, 'cart':cart}
            
            return render(request, 'payment/checkout.html', context=context)
            
        except:
            
            # Authenticated users WITH NO shipping information
            
            return render(request, 'payment/checkout.html', {'cart':cart})
    
    else:
        
        # Guest User
        
        return render(request, 'payment/checkout.html', {'cart':cart})
    
    

def complete_order(request):
    
    if request.POST.get('action') == 'post':
        
        name = request.POST.get('name')   
        email = request.POST.get('email')  
         
        address1 = request.POST.get('address1')      
        address2 = request.POST.get('address2')      
        city = request.POST.get('city')
           
        state = request.POST.get('state')   
        zipcode = request.POST.get('zipcode')   
        
        # All-in-one shipping address 
        
        shipping_address = (address1 + "\n" + address2 + "\n" 
        
        + city + "\n" + state + "\n" + zipcode
        
        )
        
        # Shopping cart information
        
        cart = Cart(request)
        
        # Get the total price of items
        
        total_cost = cart.get_total()
        
        '''
        
            Order variations
            
            1)  Create order -> Account users WITH + WITHOUT shipping information
            
            2)  Create order -> Guest users without an account
        
        '''
        
        if request.user.is_authenticated:
            
            order = Order.objects.create(
                full_name = name,
                email=email,
                shipping_address=shipping_address,
                amount_paid = total_cost, 
                user = request.user
            )
            
            order_id = order.pk
            
            for item  in cart:
                
                OrderItem.objects.create(
                    order_id=order_id,
                    product = item['product'],
                    quantity = item['qty'],
                    price = item['price'],
                    user = request.user
                )
                
        else:
            
            order = Order.objects.create(
            full_name = name,
            email=email,
            shipping_address=shipping_address,
            amount_paid = total_cost, 
            
            )
            
            order_id = order.pk
            
            
            
            for item  in cart:
                
                OrderItem.objects.create(
                    order_id=order_id,
                    product = item['product'],
                    quantity = item['qty'],
                    price = item['price'],
                )
                
        request.session['order_id'] = order_id
                
        order_success = True
        
        response = JsonResponse({'success':order_success})
        
        return response
    
    
def payment_process(request):
    # retrive the payment_id we'd set in the djago session ealier
    payment_id = request.session.get('order_id', None)
    # using the payment_id, get the database object
    payment = get_object_or_404(Order, id=payment_id)
    # retrive payment amount 
    amount = payment.get_amount()

    if request.method == 'POST':
        success_url = request.build_absolute_uri(
            reverse('payment-success'))
        cancel_url = request.build_absolute_uri(
            reverse('payment-failed'))

        # metadata to pass additional data that 
        # the endpoint doesn't accept naturally.
        metadata= json.dumps({"payment_id":payment_id,  
                              "cancel_action":cancel_url,   
                            })

        # Paystack checkout session data
        session_data = {
            'email': payment.email,
            'amount': int(amount),
            'callback_url': success_url,
            'metadata': metadata
            }

        headers = {"authorization": f"Bearer {api_key}"}
        # API request to paystack server
        r = requests.post(url, headers=headers, data=session_data)
        response = r.json()
        if response["status"] == True :
            # redirect to Paystack payment form
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass
        else:
            return render(request, 'payment/process.html', locals())
    else:
        return render(request, 'payment/process.html', locals())    
    
    


def payment_success(request):
    
    #  Clearing Shopping cart
    
    for key in list(request.session.keys()):
        
        if key == 'session_key':
            
            del request.session[key]
    
    return render(request, 'payment/payment-success.html')


def payment_failed(request):
    
    return render(request, 'payment/payment-failed.html')

