from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import CreateApplicationForm
from .models import Application


class CreateApplicationView(CreateView):
    model = Application
    template_name = 'application/create_application.html'
    form_class = CreateApplicationForm
    success_url = reverse_lazy('user:profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateApplicationView, self).form_valid(form)


class DeleteApplication(View):
    def get(self, request, pk):
        Application.objects.get(id=pk).delete()
        return redirect(reverse_lazy('user:profile'))
