from django.db import models
from django.contrib.auth.models import User


class Contract(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contracts')
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.text}'
    
    
class EmailContract(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='emails')
    fullname = models.CharField(max_length=100)


