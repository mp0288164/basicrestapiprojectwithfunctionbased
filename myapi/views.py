from django.shortcuts import render
from  rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from . serializer import MySerializer
from . models import MyApiModel


# Create your views here.
class MyApiView(APIView):
    
    def get(self,request,formate=None):
        fm=MyApiModel.objects.all()
        sm=MySerializer(fm,many=True)
        return Response({'status':'success','candidate':'sm.data'},status=status.HTTP_200_OK)
    def post(self,request,format=None,id=None,*args,**kwargs):
        sm=MySerializer(data=request.data)
        if sm.is_valid():
            sm.save()
            return Response({'msg':'datasubmitted successfully','status':'success','candidate':sm.data},status=status.HTTP_201_CREATED)
        return Response(sm.errors)
