from django.shortcuts import render,redirect
from django.contrib.auth.forms import (UserCreationForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm)
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import Identify ,registerform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProductItem,Product,ProductVariation,ProductCategory

# Create your views here.
def create_user(request):
    fm=registerform()
    context={
        'form':fm
    }
    if request.method == 'POST':
        # fm=UserCreationForm(data=request.POST)
        fm=registerform(data=request.POST)
        if fm.is_valid():
            email=fm.cleaned_data['email']
            first_name=fm.cleaned_data['first_name']
            last_name=fm.cleaned_data['last_name']
            fm.save()
            messages.success(request,'User account created successfully')
            return redirect('login')
    return render(request,'register.html',context)


def signin(request):
    fm=AuthenticationForm()
    context={
        'form':fm
    }
    if request.method == 'POST':
        fm=AuthenticationForm(data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                if user.is_authenticated:
                    login(request,user)
                    messages.success(request,'User login successfully')
                    # return redirect('home')
           #return HttpResponse('Invalid userform or password')
            else:
                 messages.error(request,'Invalid username and password')
   
    return render(request,'login.html',context)
    
@login_required(login_url='/login/')
def home(request):
    return render(request,'home.html')

def signout(request):
    logout(request)
    return redirect('login')
@login_required(login_url='/login/')
def update_password(request):
        username=request.user
        user=User.objects.get(username=username)
        fm=PasswordChangeForm(user)
        context ={
            'form':fm
        }
        if request.method == 'POST':
          fm=PasswordChangeForm(user,data=request.POST)
          if fm.is_valid():
             fm.save()
             return HttpResponse('Password  changed')
          return HttpResponse('Invalidpassword')
        return render(request,'change.html',context)

def reset_password(request,username):
    
        user=User.objects.get(username=username)
        fm=SetPasswordForm(user)
        if request.method == 'POST':
            fm=SetPasswordForm(user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'password has been reset successfully')
                return redirect("login")
            else:
                messages.error(request,'please correct errors below')
        context={
             'form':fm
        }
        return render(request,'reset.html',context)
def IdentifyView(request):
     fm=Identify()
     context={
          'form':fm
     }
     if request.method == 'POST':
          fm=Identify(request.POST)
          if fm.is_valid():
               username=fm.cleaned_data['username']
               if User.objects.filter(username=username).exists():
                    url='/resetpwd/'+username+'/'
                    return redirect(url)
               return redirect('login')
     return render(request,'identify.html',context)    


def product_list(request):
    products = ProductItem.objects.all() 
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)

# assignment traied by me:
def product_details_view(request, product_name):
    products = Product.objects.filter(product_name=product_name)
    product = products.first()
    product_items = ProductItem.objects.filter(product=product)
    product_details = []
    for item in product_items:
        variations = ProductVariation.objects.filter(product_item=item)
        size_stock_info = [
            {

                'size_name': variation.size.size_name,
                'stock': variation.qty_in_stock
            }
            for variation in variations
        ]

        product_details.append({
            'product_description': product.product_description,
            'colour': item.colour.colour_name,
            'original_price': item.original_price,
            'sale_price': item.sale_price,
            'images': [item.image1, item.image2, item.image3, item.image4],
            'sizes_and_stock': size_stock_info,
        })

    context = {
        'product_name': product.product_name,
        'product_description': product.product_description,
        'product_details': product_details,
    }

    return render(request, 'product_details.html', context)
# Methods teached by sir:
def productview(request,id):
    if ProductItem.objects.filter(product_item_id =id).exists():
        Product=ProductItem.objects.get(product_item_id =id)
        context={
            'product' : Product
        }
        return render(request,'product.html',context)
    return HttpResponse('product doesnot exist')


def products_view(request,slug):
    if ProductItem.objects.filter(slug =slug).exists():
        Product=ProductItem.objects.get(slug =slug)
        context={
            'product' : Product
        }
        return render(request,'product.html',context)
    return HttpResponse('product doesnot exist')



def categoryView(request,slug):
    if ProductCategory.objects.filter(slug=slug).exists():
        category=ProductCategory.objects.get(slug=slug)
        products=Product.objects.filter(product_category__exact= category)
        product_items=ProductItem.objects.filter(product__in=products)
        context={
            'products':product_items
        }
        return render(request,'products_category.html',context)
    return HttpResponse('Invalid category')

def homeview(request):
    categories =ProductCategory.objects.filter(category_name__in=['women kurta','mens wear TShirt','mens wear Shirt','Men kurta',
                                                                  'Womens wear Tshirt','Womens wear shirt','Jacket'])
    context={
        'categories':categories
    }
    return render(request,'phome.html',context)



          
                    
        

                    
              


