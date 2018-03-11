from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import QA
from serializers import QASerializer

from ChatBot import greetings

@api_view(['POST'])    #Only POST method will be accepted
def index(request):
	"""
	Chat API
	"""
	if request.method == 'POST':
		try:
			question = request.data["string"]
			output = greetings.get_response(question)
			time = timezone.now()

			serializer = QASerializer(data={"req_date":time, "question":question, "answere":output})
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		except Exception, e:
			print(e)
			return Response({"text":"Error in views of portfolio"}, status=status.HTTP_400_BAD_REQUEST)

