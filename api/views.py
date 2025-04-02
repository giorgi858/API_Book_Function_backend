from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics
from .serializer import BookSerializer, UserSerializer
from .models import Book
from django.contrib.auth.models import User

@api_view(['GET', 'POST'])
def api_home_page(request):
    
    if request.method == 'GET':
        
        book_queryset = Book.objects.all()
        serializeData = BookSerializer(book_queryset, many=True).data
        return Response(serializeData)
    
    if request.method == "POST":
        
        data = request.data
        serializeData = BookSerializer(data=data)
        if serializeData.is_valid():
            serializeData.save()
            return Response(serializeData.data, status=status.HTTP_201_CREATED)
        return Response(serializeData.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        
        book.delete()
        data = request.data
        serializeData = BookSerializer(book)
        return Response(serializeData.data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        data = request.data
        serializeData = BookSerializer(book, data=data)
        if serializeData.is_valid():
            serializeData.save()
            return Response(serializeData.data)
        return Response(serializeData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
