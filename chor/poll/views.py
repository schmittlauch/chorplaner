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
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))