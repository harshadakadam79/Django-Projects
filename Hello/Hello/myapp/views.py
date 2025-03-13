from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import Userserializer
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from django.http import JsonResponse
from .tasks import send_bulk_email

@api_view(['GET'])
def get_user(request):
    users = User.objects.all()  # Fetch all user records
    serializer = Userserializer(users, many=True)  # Serialize multiple records
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_user(request):
    serializer = Userserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = Userserializer(user, data=request.data, partial=True)  # Partial allows updating specific fields
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def send_mail_view(request):
    recipient_list = ['harshadakadam79@gmail.com', 'harshadakadam709@gmail.com']  # Replace with actual emails
    send_bulk_email.delay("Hello!", "This is a bulk email test.", recipient_list)
    return JsonResponse({"message": "Emails are being sent!"})


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("about")

def services(request):
    return HttpResponse("knvjnj")

def contact(request):
    return HttpResponse("conta")