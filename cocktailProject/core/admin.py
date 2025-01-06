from django.contrib import admin

from core.models import Ingredient, Cocktail,CocktailIngredient

# Register your models here.
class CocktailAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    
admin.site.register(Ingredient)

class CocktailIngredientAdmin(admin.ModelAdmin):
    list_display = ('id','ingredient','cocktail','quantity','unit')
    
    
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(CocktailIngredient, CocktailIngredientAdmin)
