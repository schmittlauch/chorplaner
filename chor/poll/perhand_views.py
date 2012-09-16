# -*- coding: latin-1 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from poll.models import Poll, Choice
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
#from django.http import Http404
#für lange Version:
#from django.template import Context, loader

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #lange Version:
    #t = loader.get_template('poll/index.html')
    #c = Context({
    #    'latest_poll_list': latest_poll_list,
    #})
    #return HttpResponse(t.render(c))
    return render_to_response('poll/index.html', {'latest_poll_list':latest_poll_list})

def detail(request, poll_id):
    #try:
    #    p = Poll.objects.get(id=poll_id)
    #except Poll.DoesNotExist:
    #    raise Http404()
    p = get_object_or_404(Poll, id=poll_id)
    return render_to_response('poll/details.html', {'poll':p}, context_instance=RequestContext(request))
    #return HttpResponse("Dies ist die Detailseite f&uuml;r Poll %s." % poll_id)

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('poll/results.html', {'poll': p})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice']) #request.POST ist ein dictionary-objekt
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('poll/details.html', {
            'poll':p, 'error_message': "Keine Antwort ausgewählt",}, context_instance=RequestContext(request))
    else:
        selected_choice.votes +=1
        selected_choice.save()
        #Verhindern von Doppelposts, wenn man auf Zurückbutton klickt:
        return HttpResponseRedirect(reverse('poll.views.results', args=(p.id,)))