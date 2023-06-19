from .models import Item
from .serializer import ItemSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view 



@api_view(['GET'])
def get_item(request):
    try:
        items = Item.objects.all()
        print(items)
        serialized = ItemSerializer(items,many = True)
        return Response(data = serialized.data, status = status.HTTP_302_FOUND)
    except Item.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    

@api_view(["GET"])
def get_one(request,pk):
    try:
        item = Item.objects.get(id = pk)
        serialized = ItemSerializer(item)
        return Response(data = serialized.data, status = status.HTTP_302_FOUND)
    except Item.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT'])
def edit_item(request,pk):
    try:
        item = Item.objects.get(id = pk)
        serialized = ItemSerializer(item,request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(data = serialized.data, status = status.HTTP_302_FOUND)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
    except Item.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_item(request):
    deserialized = ItemSerializer(data = request.data)
    if deserialized.is_valid():
        deserialized.save()
        return Response(data = deserialized.data, status = status.HTTP_201_CREATED)
    else:
        return Response(status = status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['DELETE'])
def delete_item(request,pk):
    try:
        item = Item.objects.get(id = pk)
        item.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)