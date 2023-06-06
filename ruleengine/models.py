from django.db import models

# Create your models here.

class Attribute(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField( max_length=50)
    
    def __str__(self):
        return self.name

class Rule(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField( max_length=50)
    description = models.CharField( max_length=200)
    rule_for = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='attributes')
    def __str__(self):
        return self.name

    # def get_subrules(self):
    #     return self.subrule_set.all()

    # def get_attributes(self):
    #     return self.attribute_set.all()


class SubRule(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    main_rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    description = models.CharField( max_length=200)
    rule = models.CharField( max_length=200)

    def __str__(self):
        return self.name

    def get_main_rule(self):
        return self.main_rule

    def get_attributes(self):
        return self.main_rule.attribute_set.all()

