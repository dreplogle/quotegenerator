import re
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from django.template import RequestContext

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

#class ResultsView(generic.DetailView):
#    model = Quote
#    template_name = 'quotesearch/results.html'
 
#def Results(request):

#    return 


def search(request):
    ''' Searches the quote database '''
    print("receive request for search view")
    print("RECEIVE REQUEST pre 404 " + request.POST['selection'])
    
    svalue = request.POST.get("svalue", "")
    selection = request.POST['selection']
    found_entries = None
    if ('svalue' in request.POST) and request.POST['svalue'].strip():
        query_string = request.POST['svalue']
        
        if (selection == "sauthor"):
            entry_query = get_query(query_string, ['author', ])
        elif (selection == "squote"):
            entry_query = get_query(query_string, ['quote', ])
        elif (selection == "stag"):
            entry_query = get_query(query_string, ['tag', ])       
        else:    
            entry_query = get_query(query_string, ['author', 'quote', 'tag', 'id', ])

        found_entries = Quote.objects.filter(entry_query).order_by('?')[:int(request.POST['snum'])]

    return render(request, 'quotesearch/results.html',
                          { 'query_string': query_string, 'found_entries': found_entries })
                             

    #p = get_object_or_404(Quote, pk=request.POST['svalue'])
    #print("Got this: " + p.quote + " " + p.author + " " + p.tag + " " + str(p.id))
    #return HttpResponseRedirect(reverse('quotesearch:results', args=(p.id,))) 
   

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
