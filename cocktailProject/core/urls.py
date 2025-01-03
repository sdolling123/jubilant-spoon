from django.urls import path
from .views import dashboard_view, test_one, test_two, test_three

urlpatterns = [
    path('',dashboard_view,name='dashboard'),
    path('one/',test_one,name='one'),
    path('two/',test_two,name='two'),
    path('three/',test_three,name='three'),
]
