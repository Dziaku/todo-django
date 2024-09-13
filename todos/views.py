from django.http import HttpResponse
from django.views import generic

from .models import List


class IndexView(generic.ListView):
    model = List
    paginate_by = 50

class DetailView(generic.DetailView):
    model = List