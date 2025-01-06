from django.urls import path
from .views import CocktailListView,DeleteCocktailView, test_one, test_two, test_three

urlpatterns = [
    path('',CocktailListView.as_view(),name='dashboard'),
    path('delete/<int:pk>/',DeleteCocktailView.as_view(),name='delete'),
    path('one/',test_one,name='one'),
    path('two/',test_two,name='two'),
    path('three/',test_three,name='three'),
]
