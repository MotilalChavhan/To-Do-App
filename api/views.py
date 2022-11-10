from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        confirmation = request.data['confirmation']
        if password != confirmation:
            return Response({
                "message" : "Passwords must match.",
                "status" : "fail"
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return Response({
                "message" : "Username is already taken. Try using another one.",
                "status" : "fail"
            })
        return Response({
            "message" : "Account created successfully. Sign In to create your own to-do list",
            "status" : "success"
        })

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if not user.is_authenticated:
            return Task.objects.none()
        return qs.filter(owner=user)

class TaskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'