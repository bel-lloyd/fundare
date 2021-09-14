from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dares, Dollars
from .serializers import DaresSerializer, DollarsSerializer, DaresDetailSerializer
from django.http import Http404
from rest_framework import serializers, status

class DaresList(APIView):
    def get(self, request):
        dares = Dares.objects.all()
        serializer = DaresSerializer(dares, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DaresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class DaresDetail(APIView):

    def get_object(self, pk):
        try:
            return Dares.objects.get(pk=pk)
        except Dares.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dares = self.get_object(pk)
        serializer = DaresDetailSerializer(dares)
        return Response(serializer.data)

class DollarsList(APIView):

    def get(self, request):
        dollars = Dollars.objects.all()
        serializer = DollarsSerializer(dollars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DollarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )