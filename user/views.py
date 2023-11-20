from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.core.signing import BadSignature

from .utilities import signer
from .forms import RegisterUserForm
from .models import AdvUser


class BBLoginView(LoginView):
    template_name = 'user/login.html'


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'user/logout.html'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'user/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('user:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'user/register_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'user/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'user/user_is_activated.html'
    else:
        template = 'user/activation_done.html'
        user.is_activated = True
        user.is_active = True
        user.save()
    return render(request, template)


@login_required
def profile(request):
    return render(request, 'user/profile.html')
