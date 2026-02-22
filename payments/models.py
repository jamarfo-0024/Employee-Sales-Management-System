from django.db import models
from employees.models import Employee


class Payment(models.Model):
    SALARY = 'SALARY'
    COMMISSION = 'COMMISSION'

    PAYMENT_TYPE_CHOICES = [
        (SALARY, 'Salary'),
        (COMMISSION, 'Commission'),
    ]

    PAID = 'PAID'
    UNPAID = 'UNPAID'

    STATUS_CHOICES = [
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    payment_type = models.CharField(
        max_length=20,
        choices=PAYMENT_TYPE_CHOICES
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=UNPAID
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.user.username} - {self.payment_type} - {self.status}"