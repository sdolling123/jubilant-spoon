from django.db import models

# Create your models here.
class Cocktail(models.Model):
    COCKTAIL_TYPES = [
        ('shaken', 'Shaken'),
        ('stirred', 'Stirred'),
        ('built', 'Built'),
        ('frozen', 'Frozen'),
        ('blended', 'Blended'),
    ]

    STYLE_CHOICES = [
        ('tiki', 'Tiki'),
        ('modern', 'Modern'),
        ('sour', 'Sour'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=COCKTAIL_TYPES, blank=True, null=True)
    style = models.CharField(max_length=10, choices=STYLE_CHOICES, blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    creator = models.CharField(max_length=100, blank=True, null=True)  # New field

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    TYPE_CHOICES = [
        ('spirit', 'Spirit'),
        ('modified_spirit', 'Modified Spirit'),
        ('citrus', 'Citrus'),
        ('bitters', 'Bitters'),
        ('liqueur', 'Liqueur'),
        ('sweetener', 'Sweetener'),
        ('fruit_puree', 'Fruit/Puree'),
        ('herb_spice', 'Herb/Spice'),
        ('garnish', 'Garnish'),
        ('dairy_cream', 'Dairy/Cream'),
        ('syrup_flavoring', 'Syrup/Flavoring'),
        ('vegetable', 'Vegetable'),
        ('wine_fortified_wine', 'Wine/Fortified Wine'),
        ('extract', 'Extract'),
        ('ice', 'Ice'),
    ]

    name = models.CharField(max_length=100)
    ingredient_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    brand = models.CharField(max_length=100, blank=True, null=True)
    abv = models.DecimalField("Alcohol by Volume (%)", max_digits=5, decimal_places=1, blank=True, null=True)
    sweetness = models.DecimalField("Sweetness (%)", max_digits=5, decimal_places=2, blank=True, null=True)
    acid = models.DecimalField("Acid (%)", max_digits=5, decimal_places=2, blank=True, null=True)
    instructions = models.TextField("How to create", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class CocktailIngredient(models.Model):
    cocktail = models.ForeignKey(Cocktail, related_name='ingredients', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=20, choices=[
        ('Slice', 'slice'),
        ('Wedge', 'wedge'),
        ('Drop', 'drop'),
        ('Dash', 'dash'),
        ('Milliliter', 'ml'),
        ('Ounce', 'oz'),
        ('Cup', 'c'),
    ], blank=True, null=True)
    
    def get_abbreviated_unit(self):
        abbreviations = {
            'milliliter': 'ml',
            'ounce': 'oz',
            'cup': 'c',
        }
        # Return the abbreviation if available; otherwise, return the full unit name
        return abbreviations.get(self.unit, self.unit)

    def __str__(self):
        return f'{self.quantity} {self.unit} of {self.ingredient.name}'
