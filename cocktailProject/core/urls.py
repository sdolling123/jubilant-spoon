from django.urls import path
from .views import CocktailListView,DeleteCocktailView, EditCocktailView, CreateCocktailView,DetailsCocktailView, test_one, test_two, test_three

urlpatterns = [
    path('',CocktailListView.as_view(),name='dashboard'),
    path('create/',CreateCocktailView.as_view(),name='create'),
    path('details<int:pk>/',DetailsCocktailView.as_view(),name='details'),
    path('edit/<int:pk>/',EditCocktailView.as_view(),name='edit'),
    path('delete/<int:pk>/',DeleteCocktailView.as_view(),name='delete'),
    path('one/',test_one,name='one'),
    path('two/',test_two,name='two'),
    path('three/',test_three,name='three'),
]
