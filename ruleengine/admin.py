from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import SubRule, Rule, Attribute
import rule_engine

class RuleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # rule_engine.Rule(obj)  # Apply Rule on the object
        super().save_model(request, obj, form, change)  # Save the model
    list_display = ['id','name','description']

admin.site.register(Rule, RuleAdmin)

class SubRuleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # rule_engine.Rule(obj)  # Apply Rule on the object
        super().save_model(request, obj, form, change)  # Save the model
    list_display = ['id','main_rule','rule']
admin.site.register(SubRule, SubRuleAdmin)


class AttributeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # rule_engine.Rule(obj)  # Apply Rule on the object
        super().save_model(request, obj, form, change)  # Save the model
    list_display = ['id','name']

admin.site.register(Attribute, AttributeAdmin)