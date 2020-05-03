from django import forms
from django.contrib.sites.models import Site


class AddClassForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', ]
