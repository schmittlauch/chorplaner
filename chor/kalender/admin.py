# -*- coding: utf-8 -*-
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
from kalender.models import *
from django.contrib import admin

admin.site.register(Kalender)
admin.site.register(Termin)
admin.site.register(Category)
