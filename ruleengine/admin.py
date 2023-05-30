from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import GenericRule, Rule
import rule_engine

class GenericRuleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # rule_engine.Rule(obj)  # Apply Rule on the object
        super().save_model(request, obj, form, change)  # Save the model

admin.site.register(GenericRule, GenericRuleAdmin)

class RuleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # rule_engine.Rule(obj)  # Apply Rule on the object
        super().save_model(request, obj, form, change)  # Save the model

admin.site.register(Rule, RuleAdmin)

