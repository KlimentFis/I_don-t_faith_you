from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer

class ProjectDetailAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        else:
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data)

    def post(self, request, pk=None):
        if pk is not None:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        else:
            return Response({"error": "Project ID is required for POST request."}, status=status.HTTP_400_BAD_REQUEST)


class ProjectCreateAPIView(APIView):
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllProjectsAPIView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ChangeNaebAPIView(APIView):
    def post(self, request, pk=None):
        if pk is not None:
            project = Project.objects.get(pk=pk)
            # Изменяем значение поля is_naeb на противоположное
            project.is_naeb = not project.is_naeb
            project.save()
            serializer = ProjectSerializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Project ID is required for POST request."}, status=status.HTTP_400_BAD_REQUEST)
