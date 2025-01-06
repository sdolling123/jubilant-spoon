from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView
from django.contrib import messages
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
    
class DeleteCocktailView(DeleteView):
    model = Cocktail
    template_name = "partials/delete.html"  # Optional if no template is rendered

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

    def delete(self, request, *args, **kwargs):
        """Handle DELETE requests."""
        self.object = get_object_or_404(Cocktail, pk=kwargs['pk'])
        self.object.delete()
        messages.success(request, f"The cocktail '{self.object.name}' was successfully deleted!")

        # Prepare the context for the updated list
        context = self.get_context_data()
        return render(request, 'partials/card_list.html', context)

def test_one(request):
    return render(request, "one.html")

def test_two(request):
    return render(request, "two.html")

def test_three(request):
    return render(request, "three.html")