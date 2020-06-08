from django import forms
from django.contrib.sites.models import Site


class AddAttrForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', ]
