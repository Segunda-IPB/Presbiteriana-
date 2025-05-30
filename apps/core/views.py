from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

def uph_view(request):
    return render(request, 'uph.html')

def ump_view(request):
    return render(request, 'ump.html')

def saf_view(request):
    return render(request, 'saf.html')

def ucp_view(request):
    return render(request, 'ucp.html')

def upa_view(request):
    return render(request, 'upa.html')