from django.contrib.sites.models import Site
from django.views.generic import ListView


class PaginatorListView(ListView):
    model = Site
    template_name = 'paginator/paginator.html'
    paginate_by = 1


class PaginatorInvalidAdjacentPagesListView(PaginatorListView):
    template_name = 'paginator/invalid_adjacent_pages.html'


class PaginatorInvalidAlignListView(PaginatorListView):
    template_name = 'paginator/invalid_align.html'
