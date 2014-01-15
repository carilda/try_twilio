from django.conf.urls import patterns, include, url
import answer

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thecat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hi/', 'answer.views.hi'),

#    url(r'^admin/', include(admin.site.urls)),
)
