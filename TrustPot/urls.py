from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TrustPot.views.home', name='home'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^translation/', include('translation.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
