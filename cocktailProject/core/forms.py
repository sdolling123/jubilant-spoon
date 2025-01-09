from django import forms
from .models import Cocktail, CocktailIngredient, Ingredient
import uuid


class CocktailForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = ['name', 'creator', 'type', 'style', 'instructions']
        
    name = forms.CharField(label="Name",label_suffix=":",help_text="This is a required field.",error_messages={"required":"Please fill this out"})
    instructions = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False,)
    
class CocktailIngredientForm(forms.ModelForm):
    class Meta:
        model = CocktailIngredient
        fields = ['ingredient', 'quantity', 'unit']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        unique_id = uuid.uuid4().hex  # Generate a unique ID for this form instance
        self.fields['ingredient'].widget.attrs.update({
            'class': 'hidden',
            'id': f'ingredient_id_{unique_id}',
            'name': f'ingredient_id_{unique_id}'
        })
        self.fields['quantity'].widget.attrs.update({
            # 'class': 'select-as-input',
            'id': f'ingredient_quantity_{unique_id}',
            'name': f'ingredient_quantity_{unique_id}',
            'inputmode':'decimal',
            'step': '0.01'  # Ensures browser allows decimals
        })
        self.fields['unit'].widget.attrs.update({
            # 'class': 'select-as-input',
            'id': f'ingredient_unit_{unique_id}',
            'name': f'ingredient_unit_{unique_id}'
        })
    
    # Define the 'ingredient' field as a Select field
    # ingredient = forms.ModelChoiceField(
    #     queryset=Ingredient.objects.all(),
    #     widget=forms.Select(attrs={'class': 'select-as-input', 'id':f'ingredient_name_{unique_id}'}),  # Add a class for styling/identification
    #     required=False,
    # )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        ingredient = cleaned_data.get('ingredient')

        # If quantity is provided, ingredient must also be provided
        if quantity and not ingredient:
            self.add_error('ingredient', "Ingredient is required if quantity is provided.")

        return cleaned_data