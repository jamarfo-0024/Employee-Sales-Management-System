from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Sum

from .models import Employee
from .serializers import EmployeeSerializer

from sales.models import Sale
from payments.models import Payment


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        queryset = Employee.objects.select_related('user').prefetch_related(
            'customers',
            'sales'
        )

        if user.role == 'ADMIN':
            return queryset

        return queryset.filter(user=user)


class EmployeeDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role != 'EMPLOYEE':
            return Response({"detail": "Not authorized"}, status=403)

        employee = Employee.objects.get(user=user)

        total_sales = employee.sales.count()

        total_revenue = employee.sales.aggregate(
            total=Sum('amount')
        )['total'] or 0

        total_commission = employee.sales.aggregate(
            total=Sum('commission')
        )['total'] or 0

        unpaid_payments = Payment.objects.filter(
            employee=employee,
            status='UNPAID'
        ).count()

        data = {
            "employee_id": employee.id,
            "total_sales": total_sales,
            "total_revenue": total_revenue,
            "total_commission": total_commission,
            "unpaid_payments": unpaid_payments,
        }

        return Response(data)