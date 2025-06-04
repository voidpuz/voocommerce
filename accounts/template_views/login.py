from django.views.generic import TemplateView

from accounts.forms import UserChangeForm


class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Login'
        context['form'] = UserChangeForm()
        return context