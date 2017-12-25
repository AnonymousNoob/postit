from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'postit.views.home', name='home'),
    url(r'^', include('notes.urls')),
    url(r'^notes/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
