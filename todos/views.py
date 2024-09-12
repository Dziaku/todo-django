from django.http import HttpResponse
from django.views import generic

from .models import ToDoList


class IndexView(generic.ListView):
    model = ToDoList
    paginate_by = 50

class DetailView(generic.DetailView):
    model = ToDoList