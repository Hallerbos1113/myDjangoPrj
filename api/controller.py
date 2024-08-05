import json
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def getTest(request):
  str = "<html>\
    <body>\
      <h1> Get Way </h1>\
    </body>\
  </html>" 
  return Response(str)

@api_view(['POST'])
def getPost(request, name):
  # serializer = TaskSerializer(data=request.body)
  data = (request.data)
  logger.debug(name)
  return Response(data)