from django.shortcuts import render
from django.views.generic import ListView
from .models import Cocktail

class CocktailListView(ListView):
    model = Cocktail
    template_name = "dashboard.html"  # Replace with your actual template path
    context_object_name = "cocktails"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add ingredients to the context
        context['cocktails_with_ingredients'] = [
            {
                'cocktail': cocktail,
                'ingredients': cocktail.ingredients.all()
            }
            for cocktail in self.get_queryset()
        ]
        return context

def test_one(request):
    return render(request, "one.html")

def test_two(request):
    return render(request, "two.html")

def test_three(request):
    return render(request, "three.html")