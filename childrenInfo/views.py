from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import HttpResponse

# Import model
from .models import ChildrenInfoModel
from .serializers import ChildrenInfoSerializers

def index(request):
    return HttpResponse("You're at the ChildrenInfo index.")

class ChildrenInfoView(APIView):

    #Create Method
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ChildrenInfoSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data saved successfully", status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #Read Method
    def get(self,request):
        childrenData = ChildrenInfoModel.objects.all()
        serializer = ChildrenInfoSerializers(childrenData, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #Update Method
    def put(self, request):
        data = JSONParser().parse(request)
        #format should be written in document for update
        updateData = {data['updateField']: data['updateValue']} 
        try:
            qdata = ChildrenInfoModel.objects.filter(id=data['id'])
            oldObj = qdata.first()
            newVal = {'name':oldObj.name,
                'age':oldObj.age,
                'gender':oldObj.gender,
                'school': oldObj.school}
            newVal.update(updateData)
        except:
            return Response("Invalid data to update.", status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ChildrenInfoSerializers(oldObj, data=newVal)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Delete Method
    def delete(self,request):
        data = JSONParser().parse(request)
        #send the id of the data to be deleted
        try:
            qdata = ChildrenInfoModel.objects.filter(id=data['id'])
            oldObj = qdata.first()
            oldObj.delete()
            return Response("Entry deleted.",status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Invalid data to be deleted.", status = status.HTTP_404_NOT_FOUND)