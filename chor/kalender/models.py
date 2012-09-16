# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime

#ToDo: Groups + Permissions, wer kommt?, Termin in eigenen Kalender übernehmen??

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

