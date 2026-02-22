from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet
from customers.views import CustomerViewSet
from sales.views import SaleViewSet

router = DefaultRouter()

router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'sales', SaleViewSet, basename='sale')

urlpatterns = router.urls

