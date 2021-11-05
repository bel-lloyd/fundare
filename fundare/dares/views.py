# from django.shortcuts import render
from rest_framework.fields import MISSING_ERROR_MESSAGE
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dares, Dollars
from .serializers import DaresSerializer, DollarsSerializer, DaresDetailSerializer, DollarsDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly
from rest_framework.decorators import api_view

class DaresList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            dares = Dares.objects.get(pk=pk)
            self.check_object_permissions(self.request, dares)
            return dares
        except Dares.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dares = self.get_object(pk)
        serializer = DaresDetailSerializer(dares)
        return Response(serializer.data)

    def put(self, request, pk):
        dares = self.get_object(pk)
        data = request.data
        serializer = DaresDetailSerializer(
            instance=dares,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        dares = self.get_object(pk)
        dares.delete()
        return Response(dict(message="Project successfully deleted"))

class DollarsList(APIView):

    def get(self, request):
        dollars = Dollars.objects.all()
        serializer = DollarsSerializer(dollars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DollarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

class DollarsDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnly
    ]

    def get_object(self, pk):
        try:
            dollars = Dollars.objects.get(pk=pk)
            self.check_object_permissions(self.request, dollars)
            return dollars
        except Dollars.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dollars = self.get_object(pk)
        serializer = DollarsDetailSerializer(dollars)
        return Response(serializer.data)

    def put(self, request, pk):
        dollars = self.get_object(pk)
        data = request.data
        serializer = DollarsDetailSerializer(
            instance=dollars,
            data=data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk, format=None):
        dollars = self.get_object(pk)
        dollars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)