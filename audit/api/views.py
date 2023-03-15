from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AuditQuestionSerializer
from .serializers import CompanySerializer
from audit.models import AuditQuestion
from audit.models import Company


#
# Model: Company
#


class CompanyApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    # List all
    @extend_schema(request=None, responses=CompanySerializer)
    def get(self, request, *args, **kwargs):
        """
        List all the items.
        """
        objects = Company.objects.all()
        serializer = CompanySerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#
# Model: AuditQuestion
#


class AuditQuestionApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    # List all
    @extend_schema(request=None, responses=AuditQuestionSerializer)
    def get(self, request, *args, **kwargs):
        """
        List all the items.
        """
        objects = AuditQuestion.objects.all()
        serializer = AuditQuestionSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
