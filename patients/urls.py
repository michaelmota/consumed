from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

### IMPORT ###
from .views import (
	test_view,
)

urlpatterns = [
	url(r'^$', test_view, name='test'),
]
