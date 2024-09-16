from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("list/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("addlist/", views.AddList.as_view(), name = "addlist"),
    path("list/<int:pk>/edit/", views.UpdateList.as_view(), name = "edit-list"),
    path("list/<int:pk>/delete/", views.DeleteList.as_view(), name = "delete-list"),
    path("addtask/<int:pk>/", views.AddItem.as_view(), name = "addtask"),
    path("task/<int:pk>/edit/", views.UpdateItem.as_view(), name = "edit-item"),
    path("task/<int:pk>/delete/", views.DeleteItem.as_view(), name = "delete-item"),
]