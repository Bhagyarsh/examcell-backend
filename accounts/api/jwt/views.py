# users/views.py
from rest_framework import generics
from django.contrib.auth import authenticate ,get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from django.conf import settings
from rest_framework import permissions
from rest_framework_jwt.settings import api_settings
from .utils import jwt_response_payload_handler
User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class AuthAPIView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    print("request")
    def post(self,request,*args,**kwargs):
        # payload = jwt_payload_handler(user)
        # token = jwt_encode_handler(payload)
         
        if request.user.is_authenticated:
            return Response({'detail':"you are already authenticated" },status = 400)
        else:
            print(request.method)
            print(request.POST)
            if request.POST:
                print(request)
                print(request.POST)
                email = request.POST.get('email')
                password =request.POST.get('password')
                user = authenticate(email=email,password= password)
                if user:
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)
                    return Response(jwt_response_payload_handler(token, user=user, request=request))
            return Response({'detail':"user not found at all" },status = 401)

class RegisterAPIView(generics.CreateAPIView):
    queryset =  User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

# class UpdateUser(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = ClientNameSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         print(instance)
#         serializer = self.get_serializer(instance)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         return Response(serializer.data)