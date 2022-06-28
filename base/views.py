from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import NewUserForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
class LoginInterfaceView(LoginView):
    template_name= 'base/registration/login.html'

class SignupView(CreateView):
    form_class=NewUserForm
    template_name= 'base/registration/register.html'
    success_url='/login'

    def get(self,request,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request,*args, **kwargs)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    products = Product.objects.all()

    context= dict(products=products)

    return render(request,'base/home.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created =Order.objects.get_or_create(customer=customer,complete= False)
        items = order.orderitem_set.all()
        
    
    else :
        items=[]
        order=dict(get_cart_total=0,get_cart_items=0)
    
    context = dict(items=items,order=order)
    return render(request,'base/cart.html',context)



def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created =Order.objects.get_or_create(customer=customer,complete= False)
        items = order.orderitem_set.all()
        
    
    else :
        items=[]
        order=dict(get_cart_total=0,get_cart_items=0)

    context = dict(items=items,order=order)

    return render(request,'base/checkout.html',context)