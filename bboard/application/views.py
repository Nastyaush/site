from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from .forms import CreateApplicationForm, ChangeStatusForm, CreateCategoryForm
from .models import Application, Category


class CreateApplicationView(CreateView, LoginRequiredMixin):
    model = Application
    template_name = 'application/create_application.html'
    form_class = CreateApplicationForm
    success_url = reverse_lazy('user:profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateApplicationView, self).form_valid(form)


class DeleteApplication(View, LoginRequiredMixin):
    def get(self, request, pk):
        Application.objects.get(id=pk).delete()
        return redirect(reverse_lazy('user:profile'))


class ChangeStatusView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Application
    template_name = 'application/change_status.html'
    form_class = ChangeStatusForm
    success_url = reverse_lazy('main:index')
    success_message = 'Статус изменён'


class IndexCategory(View, LoginRequiredMixin):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'application/category.html', {'categories': categories})


class DeleteCategory(View, LoginRequiredMixin):
    def get(self, request, pk):
        Category.objects.get(id=pk).delete()
        return redirect(reverse_lazy('application:index_category'))


class CreateCategory(CreateView, LoginRequiredMixin):
    model = Category
    template_name = 'application/create_category.html'
    form_class = CreateCategoryForm
    success_url = reverse_lazy('application:index_category')
