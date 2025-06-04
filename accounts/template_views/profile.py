from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Profile'
        context['current_user'] = self.request.user
        return context