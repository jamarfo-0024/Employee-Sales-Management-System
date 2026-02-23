from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Customer
from .serializers import CustomerSerializer
from employees.models import Employee


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        queryset = Customer.objects.select_related(
            'assigned_employee'
        )

        if user.role == 'ADMIN':
            return queryset

        return queryset.filter(assigned_employee__user=user)

    def perform_create(self, serializer):
        user = self.request.user

        if user.role == 'ADMIN':
            serializer.save()
            return

        employee = Employee.objects.get(user=user)
        serializer.save(assigned_employee=employee)