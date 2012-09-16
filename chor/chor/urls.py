from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('poll.urls')),
    url(r'^kalender/', include('kalender.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'kalender.views.logout_view'),
    url(r'^impressum/$', TemplateView.as_view(
        template_name="impressum.html",),name='impressum')
)
