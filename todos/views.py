from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy, reverse

from .models import List, Item


class IndexView(generic.ListView):
    model = List
    template_name = 'todos\index.html'
    paginate_by = 50

class DetailView(generic.DetailView):
    model = List

class AddList(generic.CreateView):
    model = List
    fields = ['name']

class UpdateList(generic.UpdateView):
    model = List
    fields = ['name']

class DeleteList(generic.DeleteView):
    model = List
    success_url = reverse_lazy('todos:index')

class AddItem(generic.CreateView):
    model = Item
    fields = ['list', 'task', 'deadline_date']

class UpdateItem(generic.UpdateView):
    model = Item
    fields = ['list', 'task', 'status', 'deadline_date']

class DeleteItem(generic.DeleteView):
    model = Item
    success_url = reverse_lazy('todos:index')
    