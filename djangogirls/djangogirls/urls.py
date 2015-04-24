from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangogirls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'trips.views.home'),
    url(r'^hello/$', 'trips.views.hello_world'),

]
