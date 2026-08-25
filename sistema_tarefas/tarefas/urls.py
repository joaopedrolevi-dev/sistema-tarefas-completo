from django.urls import path
from . import views

urlpatterns = [
    path("", views.tarefas, name="tarefas"),
    path("<int:id>/", views.detalhe, name="detalhe"),
]