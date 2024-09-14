from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("addlist/", views.AddList.as_view(), name = "addlist"),
    path("additem/<int:pk>/", views.AddItem.as_view(), name = "addtask"),
]