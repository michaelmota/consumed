from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

### IMPORT ###
from .views import PatientNew, PatientList

urlpatterns = [
	url(r'$', PatientList.as_view(), name="patients"),
	url(r'nuevo/$', PatientNew.as_view(), name="patient-new"),
]
