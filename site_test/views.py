from django.shortcuts import HttpResponse, render
from django.views.generic import TemplateView


class ClassEndpointView(TemplateView):
    template_name = 'home_page.html'
    http_method_names = [
        "get",
    ]

    def get(self, request, *args, **kwargs):
        return HttpResponse('page_1')


def home(request):
    return render(request, 'home_page.html')


def page_1(request):
    return render(request, 'index_1.html')


def page_2(request):
    return render(request, 'index_2.html')


def page_3(request):
    return render(request, 'index_3.html')
