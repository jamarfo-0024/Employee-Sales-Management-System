from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from employees.models import Employee
from customers.models import Customer
from sales.models import Sale
from payments.models import Payment

from django.db.models import Sum


class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role != 'ADMIN':
            return Response({"detail": "Not authorized"}, status=403)

        total_employees = Employee.objects.count()
        total_customers = Customer.objects.count()
        total_sales = Sale.objects.count()

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
            "total_customers": total_customers,
            "total_sales": total_sales,
            "total_revenue": total_revenue,
            "total_commission": total_commission,
            "unpaid_payments": unpaid_payments,
        }

        return Response(data)