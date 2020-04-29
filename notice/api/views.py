# users/views.py
from rest_framework import generics
from django.contrib.auth import authenticate ,get_user_model
from rest_framework.views import APIView
from notice.models import notice
from .serializers import NoticeSerializer
from academic.models import klass
from accounts.models import profile
from datetime import datetime
User = get_user_model()

class NoticeListApiView(generics.ListCreateAPIView):
    queryset = notice.objects.all()
    serializer_class = NoticeSerializer
    
    def get_queryset(self):
        user = self.request.user
        userprofile = profile.objects.get(user=user)
        parents = userprofile.parents
        endingdate = datetime(2022,1,1,0,0,0)
        startingdate = datetime.today()
        print(profile)
        if parents:
            return  notice.objects.filter(displaytoparents=parents).filter(displaytill__range=[startingdate,endingdate])
        return notice.objects.all().filter(displaytill__range=[startingdate,endingdate])