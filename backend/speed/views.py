from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SpeedData
from .serializers import SpeedSerializer

class LatestSpeedView(APIView):
    def get(self, request):
        speed = SpeedData.objects.last()
        if not speed:
            return Response({"speed": 0})
        return Response(SpeedSerializer(speed).data)
