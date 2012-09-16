from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
import datetime
from kalender.views import DailyView
from django.views.generic import DetailView
from kalender.models import Termin

urlpatterns = patterns('kalender.views',
    url(r'^home/$', 'kalender_home_view'),
    url(r'^(?P<calid>\d+)/(?P<year>\d+)/$', 'yearly_view',),
    url(r'^(?P<calid>\d+)/(?P<year>\d+)/(?P<month>\d+)/$', 'monthly_view',),
    url(r'^(?P<calid>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', DailyView.as_view(),name="daily_view"),
    url(r'^(?P<calid>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/new_termin/$', 'create_termin', name="date_termin"),
    url(r'^(?P<calid>\d+)/new_termin/$', 'create_termin',name="general_termin"),
    url(r'^ajax/category_suggest/$', 'category_suggest',),
    url(r'^ajax/teilnehmer_mngmt/$', 'ajax_teilnehmen'),
    url(r'^termin/(?P<pk>\d+)/$',login_required(DetailView.as_view(
        context_object_name='termin',
        model=Termin,
        )),name='termin_details'),
)
