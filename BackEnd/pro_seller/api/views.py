from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import Property
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

    
 
@api_view(['GET'])
def GetProperties(request):
    obj = Property.objects.all()
    search = request.query_params.get('search')
    if search:
        obj = obj.filter(Q(location__icontains = search) | Q(cost__icontains = search))
    serializer = PropertyGetSerializer(obj, many = True)
    return Response(serializer.data)
    
    

class PropertyViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        try:
            obj = Property.objects.filter(owner = request.user)
            if request.query_params.get('search'):
                search = request.query_params.get('search')
                obj = obj.filter(Q(location__icontains = search) | Q(cost__icontains = search))
            serializer = PropertySerializer(obj, many = True)
            return Response({"data" : serializer.data, "success" : True})
        except Exception as e:
            print(e)
            return Response({'status' : 500, "success" : False, 'message' : 'invalid Page Number', 'data' : {}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            data = request.data
            serializer = PropertySerializer(data = data)
            if serializer.is_valid():
                serializer.validated_data['owner'] = request.user
                serializer.save()
                return Response({'status' : 201, 'message' : 'blog sucessfully created', 'data' : serializer.data, "success" : True}, status = status.HTTP_201_CREATED)
            return Response({'errors' : serializer.errors,'mesage' : "bad request"})
        except Exception as e:
            return Response({'status' : 500,'error' : str(e),  'data' : {},}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    def patch(self, request):
        try:
            data = request.data
            blog = Property.objects.filter(uuid = data.get('uuid'))
            if not blog.exists():
                return Response({'status' : 404, 'message' : 'invalid uuid'}, status=status.HTTP_404_NOT_FOUND)
            if request.user != blog[0].owner:
                 return Response({'status' : 400, 'message' : 'You Are not athorized user'}, status=status.HTTP_401_UNAUTHORIZED)
            serializer = PropertySerializer(blog[0], data = data,  partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status' : 201, 'message' : 'Updated successfully', 'data' : serializer.data}, status=status.HTTP_202_ACCEPTED)        
        except Exception as e:
            print(e)
            return Response({'status' : 500, 'data' : {}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

    def delete(self, request, uuid):
        try:
            data = request.data
            blog = Property.objects.filter(uuid = uuid)
            if not blog.exists():
                return Response({'status' : 404, 'message' : 'invalid uuid'}, status=status.HTTP_404_NOT_FOUND)
            if request.user != blog[0].username:
                 return Response({'status' : 400, 'message' : 'You Are not athorized user'}, status=status.HTTP_401_UNAUTHORIZED)

            blog[0].delete()
            return Response({'status' : 201, 'message' : 'deleted successfully'}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(e)
            return Response({'status' : 500, 'data' : {}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
        
        
         
        
    
# class PublishProperty(APIView):

#     def get(self, request):
#         try:
#             obj = Property.objects.all()
#             if request.GET.get('search'):
#                 search = request.GET.get('search')
#                 obj = obj.filter(Q(title__icontains=search) | Q(descriptions__icontains=search))

#             serializer = PropertySerializer(obj, many=True)
#             return Response({'data' : serializer.data, 'success' : True})
  
#         except Exception as e:
#             return Response({'status': 500, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                    
       

    # def get_permissions(self):
    #     if self.action in ['create', 'update', 'partial_update', 'destroy']:
    #         self.permission_classes = [IsAuthenticatedOrReadOnly, IsPropertyOwner]
    #     return super(PropertyViewSet, self).get_permissions()


class IsPropertyOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user