from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class UPHView(TemplateView):
    template_name = 'uph.html'

class UMPView(TemplateView):
    template_name = 'ump.html'

class SAFView(TemplateView):
    template_name = 'saf.html'

class UCPView(TemplateView):
    template_name = 'ucp.html'

class UPAView(TemplateView):
    template_name = 'upa.html'
