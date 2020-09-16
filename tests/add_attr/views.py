from django.views.generic import FormView

from .forms import AddAttrForm


class AddAttrFormView(FormView):
    form_class = AddAttrForm
    template_name = 'add_attr/add_attr.html'
