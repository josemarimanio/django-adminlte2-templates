from django.contrib.sites.models import Site
from django.views.generic import ListView


class PaginatorListView(ListView):
    model = Site
    template_name = 'paginator.html'
    paginate_by = 1
