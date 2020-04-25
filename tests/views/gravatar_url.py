from django.views.generic import TemplateView


class GravatarUrlTemplateView(TemplateView):
    template_name = 'gravatar_url.html'

    def get_context_data(self, **kwargs):
        context = super(GravatarUrlTemplateView, self).get_context_data(**kwargs)
        context['user_obj'] = self.request.user
        return context
