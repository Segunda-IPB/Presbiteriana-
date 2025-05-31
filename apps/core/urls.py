from django.urls import path
from .views import HomeView, UPHView, UMPView, SAFView, UCPView, UPAView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('uph/', UPHView.as_view(), name='uph'),
    path('ump/', UMPView.as_view(), name='ump'),
    path('saf/', SAFView.as_view(), name='saf'),
    path('ucp/', UCPView.as_view(), name='ucp'),
    path('upa/', UPAView.as_view(), name='upa'),
]
