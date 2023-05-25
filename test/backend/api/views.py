from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SomaView(APIView):
    def post(self, request):
        var_1 = int(request.data.get('var_1'))
        var_2 = int(request.data.get('var_2'))
        resultado = var_1 + var_2
        return Response({'resultado': resultado})
# Create your views here.
