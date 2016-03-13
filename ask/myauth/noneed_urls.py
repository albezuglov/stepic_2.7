from django.conf.urls import include, url
from .views import *

urlpatterns = [
   url('^signup/$', signup, name='signup'),
   url('^login/$', login, name='login'),
]
