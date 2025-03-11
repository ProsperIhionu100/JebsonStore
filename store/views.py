from django.shortcuts import render, redirect
from .models import Category, Product, Brand, Current
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.

def home(request):
    
    all_categories = Category.objects.all()
    
    all_products = Product.objects.all()
    
    page = 1
    results = 4
    paginator = Paginator(all_products, results)
    
    products = paginator.page(page)
    
    context ={
        'products':products,
        'all_categories': all_categories
        
    }
    
    return render(request, 'store/home.html', context)


def product_page(request, slug):
    
    product = get_object_or_404(Product, slug=slug)
    
    context = {
        
        'product':product
        
    }
    
    return render(request, 'store/product_page.html', context)


def shop(request):
    
    search = request.GET.get('q') if request.GET.get('q') != None else ''


    products = Product.objects.filter(Q(brand__title__icontains=search)|Q(current__title__icontains=search))
    brand = Brand.objects.all()
    current = Current.objects.all()
    
    page = request.GET.get('page')
    results = 8
    
    paginator = Paginator(products, results)
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger :
        page =1
        products = paginator.page(page)
    except EmptyPage :
        page = paginator.num_pages
        products = paginator.page(page)
    
    leftIndex = (int(page) - 4)
    
    if leftIndex < 1:
        leftIndex = 1
        
    rightIndex = (int(page) + 5)
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
        
    custom_range = range(leftIndex, rightIndex)
        
    context ={
         
        'custom_range':custom_range,
        'current':current,
        'brand':brand,
        'products': products,
        'paginator': paginator, 
    }
    
    return render(request, 'store/shop.html', context)


def category(request, slug):
    
    category = get_object_or_404(Category, slug=slug)
    
    products = Product.objects.filter(category=category)
    
    context= {'products':products, 'category':category}
    
    return render(request, 'store/category.html', context=context)


# def cart(request):
#     return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def contact(request):
    
    if request.method == 'POST':
    
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        
        html = render_to_string('store/contactUs.html', {
            'name':name,
            'email':email,
            'message':message
        })

            # Send welcome email
        subject = name
        message = message
        from_email = email
        to_email = ['prosperbiz720@gmail.com']
        send_mail(subject, message, from_email, to_email, html_message=html, fail_silently=False)
        messages.success(request, 'we have seen the message')
        return redirect('home') 


    return render(request, 'store/contact.html')

def sign_in(request):
    return render(request, 'store/sign_in.html')

def sign_up(request):
    return render(request, 'store/sign_up.html')

def about_us(request):
    return render(request, 'store/About_us.html')


