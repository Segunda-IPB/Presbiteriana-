from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContatoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Evento, MensagemContato
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.mixins import LoginRequiredMixin

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

class FaleConoscoView(FormView):
    template_name = 'fale_conosco.html'
    form_class = ContatoForm
    success_url = reverse_lazy('fale_conosco')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AgendaView(ListView):
    model = Evento
    template_name = 'agenda.html' 
    context_object_name = 'eventos'  
    ordering = ['data', 'hora']  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        eventos = list(Evento.objects.values('titulo', 'descricao', 'data', 'hora'))
        context['eventos_json'] = json.dumps(eventos, cls=DjangoJSONEncoder)
        return context

# CRUD PARA EVENTOS 

class EventoListView(LoginRequiredMixin,ListView):
    model = Evento
    template_name = 'eventos/evento_list.html'
    context_object_name = 'eventos'

class EventoCreateView(LoginRequiredMixin,CreateView):
    model = Evento
    template_name = 'eventos/evento_form.html'
    fields = ['titulo', 'descricao', 'data', 'hora']
    success_url = reverse_lazy('evento-list')

class EventoUpdateView(LoginRequiredMixin,UpdateView):
    model = Evento
    template_name = 'eventos/evento_form.html'
    fields = ['titulo', 'descricao', 'data', 'hora']
    success_url = reverse_lazy('evento-list')

class EventoDeleteView(LoginRequiredMixin,DeleteView):
    model = Evento
    template_name = 'eventos/evento_confirm_delete.html'
    success_url = reverse_lazy('evento-list')

class EventoDetailView(LoginRequiredMixin,DetailView):
    model = Evento
    template_name = 'eventos/evento_detail.html'
    context_object_name = 'evento'

# CRUD PARA MENSAGEMCONTATO 

class MensagemListView(LoginRequiredMixin,ListView):
    model = MensagemContato
    template_name = 'mensagens/mensagem_list.html'
    context_object_name = 'mensagens'

class MensagemDetailView(LoginRequiredMixin,DetailView):
    model = MensagemContato
    template_name = 'mensagens/mensagem_detail.html'
    context_object_name = 'mensagem'

class MensagemCreateView(LoginRequiredMixin,CreateView):
    model = MensagemContato
    template_name = 'mensagens/mensagem_form.html'
    fields = ['nome', 'email', 'mensagem']
    success_url = reverse_lazy('mensagem-list')

class MensagemUpdateView(LoginRequiredMixin,UpdateView):
    model = MensagemContato
    template_name = 'mensagens/mensagem_form.html'
    fields = ['nome', 'email', 'mensagem']
    success_url = reverse_lazy('mensagem-list')

class MensagemDeleteView(LoginRequiredMixin,DeleteView):
    model = MensagemContato
    template_name = 'mensagens/mensagem_confirm_delete.html'
    context_object_name = 'mensagem'
    success_url = reverse_lazy('mensagem-list')

class PainelAdminView(LoginRequiredMixin, TemplateView):
    template_name = 'painel_admin.html'
    login_url = 'login'
