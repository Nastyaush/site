from django import forms

from .models import Application


class CreateApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('title', 'text', 'image', 'category', )
