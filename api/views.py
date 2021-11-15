
# import viewsets
from rest_framework import viewsets
from django.http import JsonResponse
import json
from django.views import View
# import local data
from .serializers import CartSerializer, CartImageSerializer
from .models import Cart, CartImage
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
@method_decorator(csrf_exempt, name='dispatch')
# Create your views here.

# create a viewset
class Home(viewsets.ModelViewSet):
    # define queryset
    queryset = Cart.objects.all()
     
    # specify serializer to be used
    serializer_class = CartSerializer
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]
class CartItemViews(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# create a viewset
class ImgDetail(viewsets.ModelViewSet):
    # define queryset
    queryset = CartImage.objects.all()
     
    # specify serializer to be used
    serializer_class = CartImageSerializer
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    
class CartImage(View):
    
    def post(self, request):        
        serializer = CartImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

       