from django.conf.urls import  url
from . import views
urlpatterns = [

    url(r'^$', views.NotesPage.as_view(), name='home'),
    url(r'^autosaveAlert$', views.autosaveAlert, name='autosaveAlert'),
    
]
