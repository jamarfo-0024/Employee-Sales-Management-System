from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from django.db.models import Sum

from .models import Employee
from .serializers import EmployeeSerializer

from sales.models import Sale
from payments.models import Payment
from activity.models import LoginLog


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


# ==============================
# EMPLOYEE DASHBOARD
# ==============================

class EmployeeDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role != 'EMPLOYEE':
            raise PermissionDenied("Not authorized")

        employee = Employee.objects.select_related('user').get(user=user)

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

        recent_sales = employee.sales.order_by('-created_at')[:5].values(
            'id',
            'amount',
            'commission',
            'created_at'
        )

        recent_logins = LoginLog.objects.filter(
            employee=employee
        ).order_by('-login_time')[:5].values(
            'login_time'
        )

        data = {
            "employee_id": employee.id,
            "stats": {
                "total_sales": total_sales,
                "total_revenue": total_revenue,
                "total_commission": total_commission,
                "unpaid_payments": unpaid_payments,
            },
            "recent_sales": list(recent_sales),
            "recent_logins": list(recent_logins),
        }

        return Response(data)


# ==============================
# ADMIN DASHBOARD SUMMARY
# ==============================

class AdminDashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role != 'ADMIN':
            raise PermissionDenied("Not authorized")

        total_employees = Employee.objects.count()

        total_revenue = Sale.objects.aggregate(
            total=Sum('amount')
        )['total'] or 0

        total_commission = Sale.objects.aggregate(
            total=Sum('commission')
        )['total'] or 0

        unpaid_payments = Payment.objects.filter(
            status='UNPAID'
        ).count()

        data = {
            "total_employees": total_employees,
            "total_revenue": total_revenue,
            "total_commission": total_commission,
            "unpaid_payments": unpaid_payments,
        }

        return Response(data)