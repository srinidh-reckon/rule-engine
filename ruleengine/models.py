from django.db import models

# Create your models here.


class GenericRule(models.Model):
    # gid = models.AutoField()
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    rule_des = models.CharField( max_length=200)
    left_atr = models.CharField(max_length=100)
    operator = models.CharField(max_length=10)
    right_atr = models.CharField(max_length=100)
    rule_string = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
class Rule(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    class_name = models.CharField( max_length=50)
    name = models.CharField( max_length=50)
    des = models.CharField( max_length=200)
    rule_string = models.CharField( max_length=200)
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Rule_detail", kwargs={"pk": self.pk})
