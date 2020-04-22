from django import forms
from django.contrib.sites.models import Site
from django.views.generic import FormView


class AddClassForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', ]


class AddClassFormView(FormView):
    form_class = AddClassForm
    template_name = 'add_class.html'
