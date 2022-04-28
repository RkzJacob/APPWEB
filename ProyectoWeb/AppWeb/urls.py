from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',home,name='home'),


]

