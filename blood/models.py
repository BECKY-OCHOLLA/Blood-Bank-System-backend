from django.db import models
# from patient import models as pmodels
# from donor import models as dmodels
class Stock(models.Model):
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.bloodgroup
    
    

