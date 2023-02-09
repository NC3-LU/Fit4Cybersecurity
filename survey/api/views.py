from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SurveyQuestionAnszerSerializer
from .serializers import SurveyQuestionSerializer
from survey.models import SurveyQuestion
from survey.models import SurveyQuestionAnswer


class SurveyQuestionApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = []

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the items.
        """
        objects = SurveyQuestion.objects.all()
        serializer = SurveyQuestionSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SurveyQuestionAnswerApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = []

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the items.
        """
        objects = SurveyQuestionAnswer.objects.all()
        serializer = SurveyQuestionAnszerSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
