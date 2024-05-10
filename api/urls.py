from django.urls import path
from .views import ProjectDetailAPIView, ProjectCreateAPIView, AllProjectsAPIView, ChangeNaebAPIView

urlpatterns = [
    path('is_naeb/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('is_naeb/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('all_projects/', AllProjectsAPIView.as_view(), name='all_project'),
    path('change_naeb/<int:pk>', ChangeNaebAPIView.as_view(), name='change_naeb'),
]
