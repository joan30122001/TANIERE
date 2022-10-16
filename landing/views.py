import datetime
from django.shortcuts import render
from .models import Landing
from rest_framework.response import Response
from .serializers import LandingSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import exceptions, status, generics, mixins, viewsets, permissions, serializers
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from django.http import HttpResponse



class LandingViewSet(viewsets.ViewSet):
    
    def list(self, request):
        serializer = LandingSerializer(Landing.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        landing = Landing.objects.get(id=pk)
        serializer = LandingSerializer(landing)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = LandingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        landing = Landing.objects.get(id=pk)
        serializer = LandingSerializer(instance=landing, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        landing = Landing.objects.get(id=pk)
        landing.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)