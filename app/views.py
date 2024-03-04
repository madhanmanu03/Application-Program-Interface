from django.shortcuts import render
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['GET','POST'])
@permission_classes(IsAuthenticated)
def schoolJsonData(request):
    SOD=School.objects.all()
    JOD=SchoolModelSerializer(SOD,many='True')
    jsondata=JOD.data
    return Response(jsondata)
