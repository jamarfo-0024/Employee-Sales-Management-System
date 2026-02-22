from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from employees.models import Employee


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'ADMIN':
            return Payment.objects.all()

        return Payment.objects.filter(employee__user=user)

    def perform_create(self, serializer):
        user = self.request.user

        if user.role == 'ADMIN':
            serializer.save()
        else:
            employee = Employee.objects.get(user=user)
            serializer.save(employee=employee)