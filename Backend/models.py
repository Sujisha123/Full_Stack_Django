from django.db import models

class Income(models.Model):

    category = models.CharField(max_length=200, null=True)
    amount = models.FloatField(default=0)
    date = models.DateField(null=True)


    def __str__(self):

        return f"{self.date} - {self.amount} - {self.category}"
    
class Expense(models.Model):

    category = models.CharField(max_length=200, null=True)
    amount = models.FloatField(default=0)
    date = models.DateField(null=True)


    def __str__(self):

        return f"{self.date} - {self.amount} - {self.category}"  
