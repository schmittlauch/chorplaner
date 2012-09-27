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

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import datetime
import calendar
from kalender.models import Kalender, Termin, Category
from django.http import Http404
from django.core.urlresolvers import reverse
from kalender.forms import NewTerminForm
import pprint, inspect
from django.views.generic import ListView, DetailView

month_names = "Januar Februar März April Mai Juni Juli August September Oktober November Dezember"
month_names = month_names.split()

class DailyView(ListView):
    context_object_name='termine'
    template_name='kalender/day.html'

    def get_context_data(self, **kwargs):
        dat = datetime.date(day=int(self.kwargs['day']),month=int(self.kwargs['month']),year=int(self.kwargs['year']))
        prev = dat - datetime.timedelta(days=1)
        nxt = dat + datetime.timedelta(days=1)
        context = super(DailyView,self).get_context_data(**kwargs)
        context['calid'] = self.kwargs['calid']
        context['day'] = self.kwargs['day']
        context['year'] = self.kwargs['year']
        context['month'] = self.kwargs['month']
        context['month_name'] = month_names[int(self.kwargs['month'])-1]
        context['next_month'] = nxt.month
        context['next_day'] = nxt.day
        context['prev_month'] = prev.month
        context['prev_day'] = prev.day
        return context
    def get_queryset(self, **kwargs):
        dat = datetime.date(day=int(self.kwargs['day']),month=int(self.kwargs['month']),year=int(self.kwargs['year']))
        return(Termin.objects.filter(date=dat).order_by('time'))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DailyView, self).dispatch(*args, **kwargs)

       
def logout_view(request):
    logout(request)
    return render_to_response('login.html', { "error_message" :"Erfolgreich ausgeloggt" ,}, context_instance=RequestContext(request))

@login_required
def yearly_view(request, calid, year):
    year = int(year)
    k = get_object_or_404(Kalender, pk=calid)
    termin_set =  k.termin_set.filter
    today = datetime.date.today()
    now_year, now_month = today.year, today.month
    month_list = []
    is_current = False
    for month_num, month_name in enumerate(month_names):
        month_num +=1
        has_entry = termin_set(
            date__year=year,
            date__month=month_num
           ).count() > 0
        is_current = year == now_year and month_num == now_month
        month_list.append([
             month_num,
             month_name,
             has_entry,
             is_current,
             ])
        
    
    return render_to_response("kalender/year.html", {'months':month_list,'year':year,'calid':calid, 'ny':now_year, 'nm':now_month,}, context_instance=RequestContext(request))

week_short = "Mo Di Mi Do Frei Sa So"
week_short = week_short.split()

@login_required
def monthly_view(request, calid, year, month):
    calid = int(calid)
    year = int(year)
    month = int(month)
    k = get_object_or_404(Kalender, pk=calid)
    termin_set = k.termin_set.filter
    today = datetime.date.today()
    now_year, now_month, now_day = today.year, today.month, today.day
    cal = calendar.Calendar()
    month_days_final = []
    try:
        month_days = tuple(cal.itermonthdays(int(year), int(month)))
    except ValueError:
        raise Http404()
    for i in range(len(month_days)):
        if month_days[i] != 0:
            entry_count = termin_set(
                date__year=year,
                date__month=month,
                date__day=month_days[i]
                ).count()
            linebreak = ((i+1) % 7) == 0
            is_current = month_days[i] == now_day and month == now_month and year == now_year
            month_days_final.append((month_days[i],entry_count, linebreak, is_current,))
        else:
            month_days_final.append((month_days[i], None, None, None))
    next_year = year+1 if month==12 else year
    prev_year = year-1 if month==1 else year
    next_month = 1 if month==12 else month+1
    prev_month = 12 if month==1 else month-1
    return render_to_response("kalender/month.html", {'days':month_days_final, 'year':year, 'month_num':month, 'week_short':week_short,'prev_year':prev_year, 'prev_month':prev_month, 'prev_month_name':month_names[prev_month-1], 'current_month_name':month_names[month-1], 'next_year':next_year, 'next_month':next_month,'next_month_name':month_names[next_month-1], 'calid':calid,}, context_instance=RequestContext(request))

#@login_required    
def category_suggest(request):
    if request.method == "GET":
        return_categories = ''
        received_str = request.GET['str']
        found_categories = Category.objects.filter(name__istartswith=received_str) #i stands for incasesensitive
        if found_categories:
            for cat in found_categories:
                return_categories = return_categories + cat.name + "\n"
        
        print "returned str:"
        print return_categories
        return HttpResponse(str(return_categories), mimetype='text/plain')
    else:
        return HttpResponse('')

@login_required
def create_termin(request, calid, year=None, month=None, day=None):
    kalender = get_object_or_404(Kalender,pk=calid)
    if request.method == "POST":
        form = NewTerminForm(request.POST)

        if form.is_valid():
            formdata = form.cleaned_data
            term = Termin(name=formdata['name'],date=formdata['date'],time=formdata['time'],description=formdata['description'],in_calendar=kalender)
            term.save()
            if formdata['category']:
                term.category.add(formdata['category'])
                term.save()
            if formdata['participants']:
                term.participants.add(request.user)
                term.save()
            return HttpResponseRedirect(reverse('termin_details',kwargs={'pk':term.id}))

    else:
        date = datetime.date(month=int(month), day=int(day), year=int(year)) if day else None
        form = NewTerminForm(initial={'date':date,})
    return render_to_response("kalender/new_termin.html", dict(calid=calid,form=form, ),context_instance=RequestContext(request))

@login_required
def ajax_teilnehmen(request):
    if request.is_ajax and request.method == 'POST':
        termin = Termin.objects.get(pk=request.POST['t_id'])
        if int(request.POST['part']) == 1:
            termin.participants.add(request.user)
            response = 'Du nimmst jetzt teil'
        elif int(request.POST['part']) == 0:
            termin.participants.remove(request.user)
            response = 'Du nimmst nicht mehr teil'
        termin.save()
        return HttpResponse(response)

@login_required
def kalender_home_view(request):
    today = datetime.datetime.today()
    kalender = Kalender.objects.all()
    #next_7_days = Termin.objects.filter(datetime.datetime(day=date.day, month=date.month, year=date.year, hour=time.hour, minute=time.minute)<today+datetime.timedelta(days=7),today>datetime.datetime(day=date.day, month=date.month, year=date.year, hour=time.hour, minute=time.minute)).order_by('date').order_by('time')
    next_7_days = Termin.objects.filter(date__gte=today.date()).filter(date__lte=(today.date()+datetime.timedelta(days=7))).order_by('date')
    return render_to_response("kalender/home.html",{'day':today.day,'month':today.month,'month_name':month_names[today.month-1],'year':today.year,'Kalender':kalender,'next_7_days':next_7_days},context_instance=RequestContext(request))
