from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'isa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^story1/$', 'story1.views.index'),
    url(r'^story1/display-library/$', 'story1.views.compound_list'),
    url(r'^admin/', include(admin.site.urls)),
)
