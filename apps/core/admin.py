from django.contrib import admin
from .models import Evento, Sociedade, Pessoa, Diretoria, MensagemContato

admin.site.register(Evento)
admin.site.register(Sociedade)
admin.site.register(Pessoa)
admin.site.register(Diretoria)
admin.site.register(MensagemContato)
