from django import forms

from .models import Application, Category


class CreateApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('title', 'text', 'image', 'category',)


class ChangeStatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('status',)


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
