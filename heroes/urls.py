from django.urls import path
from .views import heroesListView, heroesDetailView, heroesCreateView, heroesUpdateView, heroesDeleteView

urlpatterns = [
    path('', heroesListView.as_view(), name='heroes-list'),
    path('<int:pk>/', heroesDetailView.as_view(), name='heroes-detail'),
    path('create/', heroesCreateView.as_view(), name='heroes-create'),
    path('<int:pk>/update/', heroesUpdateView.as_view(), name='heroes-update'),
    path('<int:pk>/delete/', heroesDeleteView.as_view(), name='heroes-delete'),
]