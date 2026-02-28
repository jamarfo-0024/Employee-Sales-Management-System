from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from employees.views import EmployeeDashboardView, AdminDashboardSummaryView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),

    path('api/employees/me/', EmployeeDashboardView.as_view()),
    path('api/dashboard/summary/', AdminDashboardSummaryView.as_view()),

    path('api/', include('core.api_router')),
]