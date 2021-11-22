# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from survey.models import Translation
from .serializers import TranslationSerializer


class TranslationListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the Translation items for given requested user
        """
        translations = Translation.objects.all()
        serializer = TranslationSerializer(translations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        Create the Translation with given translation data
        """
        data = {
            "original": request.data.get("original"),
            "translated": request.data.get("translated"),
            "lang": request.data.get("lang"),
        }
        serializer = TranslationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TranslationDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, translation_id):
        """
        Helper method to get the object with given translation_id.
        """
        try:
            return Translation.objects.get(id=translation_id)
        except Translation.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, translation_id, *args, **kwargs):
        """
        Retrieves the Todo with given translation_id
        """
        translation_instance = self.get_object(translation_id)
        if not translation_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = TranslationSerializer(translation_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, translation_id, *args, **kwargs):
        """
        Updates the todo item with given translation_id if exists
        """
        translation_instance = self.get_object(translation_id)
        if not translation_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "original": request.data.get("original"),
            "translated": request.data.get("translated"),
            "lang": request.data.get("lang"),
        }
        serializer = TranslationSerializer(
            instance=translation_instance, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, translation_id, *args, **kwargs):
        """
        Deletes the todo item with given translation_id if exists
        """
        translation_instance = self.get_object(translation_id)
        if not translation_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        translation_instance.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
