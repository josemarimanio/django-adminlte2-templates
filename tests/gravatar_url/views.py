from django.views.generic import TemplateView


class GravatarUrlTemplateView(TemplateView):
    template_name = 'gravatar_url/gravatar_url.html'

    def get_context_data(self, **kwargs):
        context = super(GravatarUrlTemplateView, self).get_context_data(**kwargs)
        context['user_obj'] = self.request.user
        return context


class GravatarUrlInvalidDefaultTemplateView(TemplateView):
    template_name = 'gravatar_url/invalid_default.html'


class GravatarUrlInvalidSizeMinTemplateView(TemplateView):
    template_name = 'gravatar_url/invalid_size_min.html'


class GravatarUrlInvalidSizeMaxTemplateView(TemplateView):
    template_name = 'gravatar_url/invalid_size_max.html'


class GravatarUrlInvalidRatingTemplateView(TemplateView):
    template_name = 'gravatar_url/invalid_rating.html'
