from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.NoteList.as_view() , name='home'),
    url(r'^(?P<pk>[0-9]+)$', views.NoteDetail.as_view(),name='note_detail'),
    url(r'^version/(?P<pk>[0-9]+)$', views.NoteHistory.as_view(),name='note_history'),
    url(r'^update/(?P<pk>[0-9]+)$', views.NoteUpdate.as_view(),name='note_update'),
    url(r'^create/$', views.NoteCreate.as_view(),name='note_create'),

]
