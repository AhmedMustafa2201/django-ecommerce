from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.hashers import make_password
# from django.http import HttpResponse

from .models import Product, User
from .forms import UserForm

# Create your views here.

def welcome(request):
    return render(request, 'website/welcome.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'website/products.html', { "products": products })

def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    similar_products = Product.objects.all().exclude(pk=id)[:2]
    return render(request, 'website/product_details.html', { "product": product, "similar_products": similar_products })

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # encrypt password before saving it.
            encrypted_password = make_password(request.POST["Password"])
            user = User(Name= request.POST["Name"],Email=request.POST["Email"], Password=encrypted_password)
            user.save()
            return redirect('home_page')
    else:
        form = UserForm()

    return render(request, 'website/register.html', {"form": form})
