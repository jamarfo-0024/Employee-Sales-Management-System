from django.db import models
from employees.models import Employee

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    assigned_employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='customers'
    )

    def __str__(self):
        return self.name
