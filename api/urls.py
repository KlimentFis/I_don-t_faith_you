from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from .views import ProjectDetailAPIView, ProjectCreateAPIView, AllProjectsAPIView, ChangeNaebAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="API Документация",
      default_version='v1',
      description="API Документация",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@onlinelessons.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('is_naeb/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('is_naeb/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('all_projects/', AllProjectsAPIView.as_view(), name='all_project'),
    path('change_naeb/<int:pk>', ChangeNaebAPIView.as_view(), name='change_naeb'),
    path('swagger-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
