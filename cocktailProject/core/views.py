from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, DetailView, TemplateView
from django.contrib import messages
from .models import Cocktail, CocktailIngredient
from .forms import CocktailForm, CocktailIngredientForm


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

class CreateCocktailView(TemplateView):
    def get(self, request):
            cocktail_form = CocktailForm()
            ingredient_form = CocktailIngredientForm()
            return render(request, 'cocktails/create.html', {
                'cocktail_form': cocktail_form,
                'ingredient_form': ingredient_form
            })

    def post(self, request):
        cocktail_form = CocktailForm(request.POST)
        print("cocktail form", cocktail_form)
        # Extract ingredient data grouped by UUID
        print("ingredient form", request.POST.items())
        ingredient_data = {}
        for key, value in request.POST.items():
            print("key: ",key)
            print("value: ", value)
            if key.startswith("ingredient_id_"):
                uuid = key.split("_")[-1]
                ingredient_data.setdefault(uuid, {})['ingredient'] = value
            elif key.startswith("ingredient_quantity_"):
                uuid = key.split("_")[-1]
                ingredient_data.setdefault(uuid, {})['quantity'] = value
            elif key.startswith("ingredient_unit_"):
                uuid = key.split("_")[-1]
                ingredient_data.setdefault(uuid, {})['unit'] = value

        print("Ingredient Data:", ingredient_data)  # Debugging

        if cocktail_form.is_valid():
            # Save the cocktail
            cocktail = cocktail_form.save()

            # Process each set of ingredient data
            ingredient_forms = []
            for uuid, data in ingredient_data.items():
                ingredient_form = CocktailIngredientForm(data)
                ingredient_forms.append(ingredient_form)

                if ingredient_form.is_valid():
                    ingredient = ingredient_form.save(commit=False)
                    ingredient.cocktail = cocktail
                    ingredient.save()
                else:
                    print("Ingredient Form Errors:", ingredient_form.errors)  # Debugging
                    # If any ingredient form is invalid, return the form with errors
                    return render(request, 'cocktails/create.html', {
                        'cocktail_form': cocktail_form,
                        'ingredient_form': CocktailIngredientForm(),
                        'ingredient_forms': ingredient_forms,  # Include all forms for error display
                    })
             # Add a success message
            messages.success(self.request, f"The cocktail '{cocktail.name}' was successfully added!")
            return redirect('dashboard')  # Redirect to the cocktail list view

        return render(request, 'cocktails/create.html', {
            'cocktail_form': cocktail_form,
            'ingredient_form': CocktailIngredientForm(),
        })



class DetailsCocktailView(DetailView):
    pass

class EditCocktailView(DetailView):
    pass

def test_one(request):
    return render(request, "one.html")

def test_two(request):
    return render(request, "two.html")

def test_three(request):
    return render(request, "three.html")