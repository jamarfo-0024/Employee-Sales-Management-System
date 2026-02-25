from rest_framework import serializers
from .models import Employee
from customers.serializers import CustomerSerializer
from sales.serializers import SaleSerializer


class EmployeeSerializer(serializers.ModelSerializer):

    customers = CustomerSerializer(
        many=True,
        read_only=True,
    )

    sales = SaleSerializer(
        many=True,
        read_only=True
    )

    total_commission_earned = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    def get_total_commission_earned(self, obj):
        return sum(sale.commission for sale in obj.sales.all())