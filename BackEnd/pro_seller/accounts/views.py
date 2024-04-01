from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

# Create your views here.

class RegisterApi(APIView):
    def get(self, request):
        try:
            obj = User.objects.all()[0]
            serializer = UserRegister(obj)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({'status' : 400, 'data' : {},"success" : False, 'message' : 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def post(self, request):
        try:        
            data = request.data
            serializer = UserRegister(data = data)
            if not serializer.is_valid():
                return Response({'status' : 404, 'message' : 'something went wrong',"success" : False, 'error' : serializer.errors},status = status.HTTP_400_BAD_REQUEST)   
            serializer.save()
            return Response({'status' : 201, 'message' : 'Account Creted', "success" : True, 'data' : serializer.data,}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({'status' : 400, 'data' : {},"success" : False, 'message' : 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request):
        data = request.data
        
        obj = User.objects.filter(id = data.get('id'))
        if not obj.exists(): 
            return Response({'errors' : "Invalid id"})
        
        serializer = UserRegister(obj[0], data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data})
        
        return Response({"errors" : serializer.errors})

class LoginApi(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if serializer.is_valid():
            response = serializer.get_token(data)
            return Response({'data' : serializer.data, 'response' : response}, status=status.HTTP_201_CREATED)
        
        return Response({'errors' : serializer.errors})