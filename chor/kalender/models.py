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

from django.db import models
from django.contrib.auth.models import User
import datetime


class Kalender(models.Model):
    name = models.CharField("Kalendername", max_length=100)
    description = models.TextField("Beschreibung")
    
    class Meta:
        verbose_name_plural = "Kalender"
    
    def __unicode__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField("Kategoriename", max_length=100, primary_key=True) 
    
    def __unicode__(self):
        return self.name

class Termin(models.Model):
    name = models.CharField("Terminname", max_length=100)
    date = models.DateField("Datum")
    time = models.TimeField("Uhrzeit")
    description = models.TextField("Beschreibung")
    in_calendar = models.ForeignKey(Kalender, blank=True)
    
    def is_today(self):
        return self.date == datetime.date.today()
    
    is_today.short_description = "Termin findet heute statt?"

    def is_next_7_days(self):
        return(self.date <= datetime.date.today() + datetime.timedelta(days=7) and datetime.datetime.today >= datetime.datetime(day=self.date.day, month=self.date.month, year=self.date.year, hour=self.time.hour, minute=self.time.minute))
    
    participants = models.ManyToManyField(User, blank=True,verbose_name="Nimmst du teil?")
    category = models.ManyToManyField(Category, blank=True,verbose_name="Kategorie")
    
    class Meta:
        verbose_name_plural = "Termine"
    
    def __unicode__(self):
        return self.name

