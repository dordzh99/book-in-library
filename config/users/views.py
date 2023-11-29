from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CustomUserSerializer
from .tasks import send_message

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_message.delay(user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
