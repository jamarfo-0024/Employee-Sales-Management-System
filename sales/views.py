from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Sale
from .serializers import SaleSerializer
from employees.models import Employee


class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'ADMIN':
            return Sale.objects.all()

        return Sale.objects.filter(employee__user=user)

    def perform_create(self, serializer):
        user = self.request.user

        if user.role == 'ADMIN':
            serializer.save()
        else:
            employee = Employee.objects.get(user=user)
            serializer.save(employee=employee)