from django.db import models

# Create your models here.
from django.db import models
from employees.models import Employee
from customers.models import Customer


class Sale(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='sales')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.commission = self.amount * (self.employee.commission_rate / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.user.username} - {self.amount}"