from django.http import Http404, HttpResponse
from django.shortcuts import render

from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template

from application.models import Application


def index(request):
    applications = Application.objects.all()
    return render(request, 'main/index.html', {'applications': applications})


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
