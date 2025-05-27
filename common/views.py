from django.views.generic import TemplateView

from products.models import Category


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()

        context['title'] = 'VooCommerce | Home'
        context['categories'] = categories
        print(categories[1].image.url)
        return context
    

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Contact Us'
        return context
    

class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    

class BlogDetailView(TemplateView):
    template_name = 'blog-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Blog Detail'
        return super().get_context_data(**kwargs)


class ShopGridView(TemplateView):
    template_name = 'shop-grid.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    

class ShopDetailsView(TemplateView):
    template_name = 'shop-details.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    

class ShoppingCartView(TemplateView):
    template_name = 'shopping-cart.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)