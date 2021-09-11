from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dares
from .serializers import DaresSerializer

class DaresList(APIView):
    def get(self, request):
        dares = Dares.objects.all()
        serializer = DaresSerializer(dares, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)