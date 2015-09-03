from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Category, Graph

class IndexView(generic.ListView):
    template_name = 'graphs/index.html'
    context_object_name = 'latest_category_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Category.objects.order_by('name')

class DetailView(generic.DetailView):
    model = Category
    template_name = 'graphs/detail.html'

'''
def index(request):
    latest_category_list = Category.objects.order_by('name')
    context = {'latest_category_list': latest_category_list}
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