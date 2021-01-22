from django.conf.urls import url
from BibliotekaApp import views


urlpatterns = [
    url(r'^knjige/$', views.knjigeApi),
    url(r'^knjige/([0-9]+)$', views.knjigeApi),
    url(r'^clan/$', views.clanApi),
    url(r'^clan/([0-9]+)$', views.clanApi)
]
