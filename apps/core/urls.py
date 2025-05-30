from django.urls import path
from .views import Home, uph_view, ump_view, saf_view, ucp_view, upa_view

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('uph/', uph_view, name='uph'),
    path('ump/', ump_view, name='ump'),
    path('saf/', saf_view, name='saf'),
    path('ucp/', ucp_view, name='ucp'),
    path('upa/', upa_view, name='upa'),
]
