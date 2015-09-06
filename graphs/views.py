from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Min

from .models import Category, Graph, Scategory, States

class IndexView(generic.ListView):
    template_name = 'graphs/index.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        #Return the categories."""
        #return Scategory.objects.order_by('series_id')
        return Scategory.objects.values("category1__name",
            "category2__name",
            "category3__name",
            "category4__name",
            "category5__name",
            "category6__name",
            "category7__name",
            "category8__name",
            "category9__name",
            "category1",
            "category2",
            "category3",
            "category4",
            "category5",
            "category6",
            "category7",
            "category8",
            "category9"
            ).annotate(series_id=Min('series_id'))

class DetailView(generic.DetailView):
    template_name = 'graphs/detail.html'
    model = Scategory

'''
def index(request):
    category_list = Category.objects.order_by('name')
    context = {'category_list': category_list}
    return render(request, 'graphs/index.html', context)

def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'graphs/detail.html', {'category': category})

def results(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'graphs/results.html', {'category': category})
'''
def vote(request, category_id):
    p = get_object_or_404(Category, pk=category_id)
    try:
        selected_graph = p.graph_set.get(pk=request.POST['graph'])
    except (KeyError, Category.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'graphs/detail.html', {
            'category': p,
            'error_message': "You didn't select a graph.",
        })
    else:
        selected_graph.votes += 1
        selected_graph.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('graphs:detail', args=(p.id,)))