from django.shortcuts import render

from django.contrib.auth import login, logout, authenticate

from rest_framework import generics, status, pagination
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *
from .permissions import *


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10  # Customize the number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]    

class RetrieveIntentView(generics.RetrieveAPIView):
    # GET
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class CreateIntentView(generics.CreateAPIView):
    # POST
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class UpdateIntentView(generics.UpdateAPIView):
    # PUT and PATCH
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class ListCreateIntentView(generics.ListCreateAPIView):
    # GET and POST
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = CustomPagination


    def create(self, request, *args, **kwargs):
        intents_data = request.data
        serializer = self.get_serializer(data = intents_data, many = isinstance(intents_data, list))
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status = status.HTTP_201_CREATED, headers = headers)

    def perform_create(self, serializer):
        serializer.save()

class DeleteIntentView(generics.DestroyAPIView):
    # DELETE
    queryset = Intent.objects.all()
    serializers_class = IntentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_202_ACCEPTED)
    

class RetrievePatternView(generics.RetrieveAPIView):
    # GET
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]    

class CreatePatternView(generics.CreateAPIView):
    # POST
    queryset = Intent.objects.all()
    serializer_class = PatternSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class UpdatePatternView(generics.UpdateAPIView):
    # PUT and PATCH
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class ListCreatePatternView(generics.ListCreateAPIView):
    # GET and POST
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        patterns_data = request.data
        serializer = self.get_serializer(data = patterns_data, many = isinstance(patterns_data, list))
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status = status.HTTP_201_CREATED, headers = headers)

    def perform_create(self, serializer):
        serializer.save()

class DeletePatternView(generics.DestroyAPIView):
    # DELETE
    queryset = Pattern.objects.all()
    serializers_class = PatternSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_202_ACCEPTED)



    
class RetrieveAnswerView(generics.RetrieveAPIView):
    # GET
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]    

class CreateAnswerView(generics.CreateAPIView):
    # POST
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class UpdateAnswerView(generics.UpdateAPIView):
    # PUT and PATCH
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class ListCreateAnswerView(generics.ListCreateAPIView):
    # GET and POST
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = CustomPagination
    
    def create(self, request, *args, **kwargs):
        answers_data = request.data
        serializer = self.get_serializer(data = answers_data, many = isinstance(answers_data, list))
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status = status.HTTP_201_CREATED, headers = headers)

    def perform_create(self, serializer):
        serializer.save()

class DeleteAnswerView(generics.DestroyAPIView):
    # DELETE
    queryset = Answer.objects.all()
    serializers_class = AnswerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_202_ACCEPTED)


