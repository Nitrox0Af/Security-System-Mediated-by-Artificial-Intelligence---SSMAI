from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import resultado

class SomaView(APIView):
    def post(self, request):
        var_1 = int(request.data.get('var_1'))
        var_2 = int(request.data.get('var_2'))
        res1 = var_1 + var_2
        res2 = resultado(res=res1)
        res2.save()
        return Response({'resultado': res1})
# Create your views here.
