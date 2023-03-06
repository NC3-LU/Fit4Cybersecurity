from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RecommendationsSerializer
from .serializers import SurveyQuestionAnszerSerializer
from .serializers import SurveyQuestionSerializer
from .serializers import SurveySectionSerializer
from .serializers import SurveyUserAnswerSerializer
from .serializers import SurveyUserSerializer
from survey.models import Recommendations
from survey.models import SurveyQuestion
from survey.models import SurveyQuestionAnswer
from survey.models import SurveySection
from survey.models import SurveyUser
from survey.models import SurveyUserAnswer


#
# Model: Recommendations
#


class RecommendationsApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    # List all
    @extend_schema(request=None, responses=RecommendationsSerializer)
    def get(self, request, *args, **kwargs):
        """
        List all the items.
        """
        objects = Recommendations.objects.all()
        serializer = RecommendationsSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#
# Model: SurveySection
#


class SurveySectionApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    # List all
    @extend_schema(request=None, responses=SurveySectionSerializer)
    def get(self, request, *args, **kwargs):
        """
        List all the items.
        """
        objects = SurveySection.objects.all()
        serializer = SurveySectionSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#
# Model: SurveyQuestion
#


class SurveyQuestionApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    # List all
    @extend_schema(request=None, responses=SurveyQuestionSerializer)
    def get(self, request, *args, **kwargs):
        """
        List all the items.
        """
        objects = SurveyQuestion.objects.all()
        serializer = SurveyQuestionSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#
# Model: SurveyQuestionAnswer
#


class SurveyQuestionAnswerApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    # List all
    @extend_schema(request=None, responses=SurveyQuestionAnszerSerializer)
    def get(self, request, *args, **kwargs):
        """
        List all the items.
        """
        objects = SurveyQuestionAnswer.objects.all()
        serializer = SurveyQuestionAnszerSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#
# Model: SurveryUser
#


class SurveyUsersApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = SurveyUser.objects.all().order_by("-created_at")

    # List all
    @extend_schema(request=None, responses=SurveyUserSerializer)
    def get(self, request):
        """
        Get all the items.
        """
        objects = SurveyUser.objects.all()
        serializer = SurveyUserSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SurveyUserApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    # Get an elemtent
    @extend_schema(request=None, responses=SurveyUserSerializer)
    def get(self, request, id):
        """
        Get an item.
        """
        objects = SurveyUser.objects.filter(user_id=id)
        serializer = SurveyUserSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#
# Model: SurveryUserAnswer
#


class SurveyUserAnswerApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    # Get an elemtent
    @extend_schema(request=None, responses=SurveyUserAnswerSerializer)
    def get(self, request, id):
        """
        Get an item.
        """
        objects = SurveyUserAnswer.objects.filter(user__user_id=id)
        serializer = SurveyUserAnswerSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
