from django.views.generic import FormView

from .forms import AddClassForm


class AddClassFormView(FormView):
    form_class = AddClassForm
    template_name = 'add_class/add_class.html'
