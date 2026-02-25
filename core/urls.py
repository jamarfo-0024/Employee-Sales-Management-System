from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import DashboardSummaryView
from employees.views import EmployeeDashboardView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),

    path('api/', include('core.api_router')),

    path('api/dashboard/summary/', DashboardSummaryView.as_view()),

    path('api/employee/dashboard/', EmployeeDashboardView.as_view()),
]
