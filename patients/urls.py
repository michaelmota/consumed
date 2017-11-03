from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

### IMPORT ###
from .views import PatientNew, PatientList, PatientEdit, PatientDelete, PatientDetailView
from .views import TherapyNew, TherapyList

urlpatterns = [
    url(r'list/$', PatientList.as_view(), name="patient-list"),
    url(r'nuevo/$', PatientNew.as_view(), name="patient-new"),
    url(r'ver/(?P<pk>.*)/$', PatientDetailView.as_view(), name="patient-view"),
    url(r'editar/(?P<pk>.*)/$', PatientEdit.as_view(), name="patient-edit"),
    url(r'eliminar/(?P<pk>.*)/$', PatientDelete.as_view(), name="patient-delete"),
    # Therapy's
    url(r'ver/terapias/(?P<pk>.*)$', TherapyList, name="therapy-list"),
    url(r'terapias/new/$', TherapyNew.as_view(), name="therapy-new"),
    # Tests
]
