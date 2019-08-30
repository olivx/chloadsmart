from django.shortcuts import render

# Create your views here.


def index(request):
    return render(template_name="index.html", request=request, context={})


def list_cargos(request):
    pass


def list_truks(request):
    pass


def detail_cargos(request):
    pass


def detail_truks(request):
    pass
