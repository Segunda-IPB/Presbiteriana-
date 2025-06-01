from django.urls import path
from .views import (
    HomeView, UPHView, UMPView, SAFView, UCPView, UPAView,
    FaleConoscoView, AgendaView,
    EventoListView, EventoCreateView, EventoUpdateView,
    EventoDeleteView, EventoDetailView, MensagemListView, MensagemDetailView,
    MensagemCreateView, MensagemUpdateView, MensagemDeleteView, PainelAdminView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('uph/', UPHView.as_view(), name='uph'),
    path('ump/', UMPView.as_view(), name='ump'),
    path('saf/', SAFView.as_view(), name='saf'),
    path('ucp/', UCPView.as_view(), name='ucp'),
    path('upa/', UPAView.as_view(), name='upa'),
    path('fale-conosco/', FaleConoscoView.as_view(), name='fale_conosco'),
    path('agenda/', AgendaView.as_view(), name='agenda'), 
    path('eventos/', EventoListView.as_view(), name='evento-list'),
    path('eventos/criar/', EventoCreateView.as_view(), name='evento-create'),
    path('eventos/<int:pk>/editar/', EventoUpdateView.as_view(), name='evento-update'),
    path('eventos/<int:pk>/excluir/', EventoDeleteView.as_view(), name='evento-delete'),
    path('eventos/<int:pk>/', EventoDetailView.as_view(), name='evento-detail'),
    path('mensagens/', MensagemListView.as_view(), name='mensagem-list'),
    path('mensagens/criar/', MensagemCreateView.as_view(), name='mensagem-create'),
    path('mensagens/<int:pk>/', MensagemDetailView.as_view(), name='mensagem-detail'),
    path('mensagens/<int:pk>/editar/', MensagemUpdateView.as_view(), name='mensagem-update'),
    path('mensagens/<int:pk>/excluir/', MensagemDeleteView.as_view(), name='mensagem-delete'),
    path('painel/', PainelAdminView.as_view(), name='painel-admin'),
]
