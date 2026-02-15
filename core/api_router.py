from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet
from customers.views import CustomerViewSet

router = DefaultRouter()

router.register(r'employees', EmployeeViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = router.urls
