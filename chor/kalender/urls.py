#Copyright (C) 2012  Oliver Schmidt
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as
#published by the Free Software Foundation, either version 3 of the
#License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.

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
