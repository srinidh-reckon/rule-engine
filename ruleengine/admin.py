from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import GenericRules, Rules
import rule_engine

class GenericRulesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # rule_engine.Rule(obj)  # Apply rules on the object
        super().save_model(request, obj, form, change)  # Save the model

admin.site.register(GenericRules, GenericRulesAdmin)

class RulesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # rule_engine.Rule(obj)  # Apply rules on the object
        super().save_model(request, obj, form, change)  # Save the model

admin.site.register(Rules, RulesAdmin)

