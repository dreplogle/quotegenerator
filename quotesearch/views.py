from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.core.context_processors import csrf

from .models import Quote 

class IndexView(generic.ListView):
    print("receive request for INDEX view")
    template_name = 'quotesearch/index.html'
    context_object_name = 'first_quotes'
    
    def get_queryset(self):
        return Quote.objects.filter(tag='age')[:5]

    
        #def get_queryset(self):
    #    """Return the last five published questions."""
    #    return Question.objects.filter(
    #        pub_date__lte=timezone.now()
    #    ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Quote
    template_name = 'quotesearch/detail.html'
    context_object_name = 'first_quotes'
    
    def get_queryset(self):
        return Quote.objects.filter(tag='age')[:5]

class ResultsView(generic.DetailView):
    model = Quote
    template_name = 'quotesearch/results.html'
    

def search(request):
    #request.POST.get("svalue", "")
    c = {}
    c.update(csrf(request))
    print("receive request for search view")
    print("RECEIVE REQUEST pre 404 " + request.POST.get("svalue", ""))
    p = get_object_or_404(Quote, pk=request.POST['svalue'])
    print("Got this: " + p.quote + " " + p.author + " " + p.tag + " " + str(p.id))
    #return HttpResponseRedirect(reverse('quotesearch:index')) 
    return HttpResponseRedirect(reverse('quotesearch:results', args=(p.id,))) 
    
    #p = get_object_or_404(Quote, pk=svalue)
    #print('RECEIVED REQUEST: ')
    #try:
    #    selected_choice = p.quote_set.get(pk=request.POST['svalue'])
    #except (KeyError, Quote.DoesNotExist):
    #    # Redisplay the question voting form.
    #    return render(request, 'quotesearch/index.html', {
    #        'quote': p,
    #        'error_message': "Don't do that",
    #    })
    #else:
    #    return 
    #    return HttpResponseRedirect(reverse('quotesearch:results', args=(p.quote,)))
