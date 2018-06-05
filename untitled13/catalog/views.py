from django.shortcuts import get_object_or_404, render_to_response
from catalog.models import Category, Product
from django.template import RequestContext
from untitled13.cart import cart
from django.http import HttpResponseRedirect
from untitled13.catalog.forms import ProductAddToCartForm


def index(request, template_name='catalog/index.html'):
    page_title = 'online shop for all items'
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def show_category(request, category_slug, template_name='catalog/category.html'):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def show_product(request, product_slug, template_name='catalog/product.html'):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        if form.is_valid():
            cart.add_to_cart()
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = 'show_cart'
            return HttpResponseRedirect(url)
    else:
        form = ProductAddToCartForm(request=request, label_suffix=':')
        form.fields['product_slug'].widget.attrs['value'] = product_slug
        request.session.set_test_cookie()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

