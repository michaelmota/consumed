from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

### IMPORT ###
from .views import PatientNew, PatientList, PatientEdit, PatientDelete, PatientDetailView
from .views import TherapyNew, TherapyList, ClinicHistoryView

urlpatterns = [
    url(r'^$', PatientList.as_view(), name="list"),
    # Pacientes
    url(r'ver/(?P<pk>.*)/$', PatientDetailView.as_view(), name="view"),
    url(r'nuevo/$', PatientNew.as_view(), name="new"),
    url(r'editar/(?P<pk>.*)/$', PatientEdit.as_view(), name="edit"),
    url(r'eliminar/(?P<pk>.*)/$', PatientDelete.as_view(), name="delete"),
    # Terapias
    url(r'terapias/new/$', TherapyNew.as_view(), name="therapy-new"),
    url(r'ver/terapias/(?P<pk>.*)$', TherapyList, name="therapy-list"),
    # Historial Clínico
    url(r'ver/historial/(?P<id>.*)$', ClinicHistoryView, name="clinich-view"),
]
