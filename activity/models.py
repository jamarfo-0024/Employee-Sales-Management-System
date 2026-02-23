from django.db import models
from employees.models import Employee


class LoginLog(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='login_logs'
    )

    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.user.username} - {self.login_time}"