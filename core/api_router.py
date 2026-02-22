from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet
from customers.views import CustomerViewSet
from sales.views import SaleViewSet
from payments.views import PaymentViewSet

router = DefaultRouter()

router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'sales', SaleViewSet, basename='sale')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = router.urls

