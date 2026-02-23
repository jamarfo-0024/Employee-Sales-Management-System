from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

from employees.models import Employee
from .models import LoginLog


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    try:
        employee = Employee.objects.get(user=user)
        LoginLog.objects.create(employee=employee)
    except Employee.DoesNotExist:
        pass