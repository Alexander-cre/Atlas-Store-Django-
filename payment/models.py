from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    refrence = models.CharField(max_length=100 , unique=True)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user} -{self.amount}"