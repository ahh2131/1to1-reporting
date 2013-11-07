from django.conf.urls import patterns, include, url
from django.conf import settings
from reporting import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reporting.views.home', name='home'),
    # url(r'^reporting/', include('reporting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #static
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT}),

    #media
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    #index
    url(r'^$', 'reporting.views.home', name="home"),
    url(r'^dashboard1/', 'reporting.views.home', name="dashboard1"),
    url(r'^dashboard/', views.ReportingList.as_view(), name="dashboard"),
    url(r'^profile/', 'reporting.views.home', name="profile"),

    #posts
    (r'^posts/', include('posts.urls')),
)
