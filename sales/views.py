from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Sale
from .serializers import SaleSerializer
from employees.models import Employee


class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        queryset = Sale.objects.select_related(
            'employee',
            'customer'
        )

        if user.role == 'ADMIN':
            return queryset

        return queryset.filter(employee__user=user)

    def perform_create(self, serializer):
        user = self.request.user

        if user.role == 'ADMIN':
            serializer.save()
            return

        employee = Employee.objects.get(user=user)
        customer = serializer.validated_data.get('customer')

        # SECURITY VALIDATION
        if customer.assigned_employee != employee:
            raise PermissionDenied(
                "You cannot create a sale for another employee's customer."
            )

        serializer.save(employee=employee)