from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Product


def index(request):
    categories = Category.objects.filter(parent=None)
    products = Product.objects.filter(available=True)
    context = {"categories": categories, "products": products}
    return render(request, "shop/index.html", context,)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(available=True, category=category)
    if not category.parent:
        products = Product.objects.filter(category__parent__slug=category_slug, available=True)
    return render(
        request,
        "shop/shop.html",
        {"category": category, "categories": categories, "products": products},
    )

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "shop/product/detail.html",
        {"product": product, "cart_product_form": cart_product_form},
    )
