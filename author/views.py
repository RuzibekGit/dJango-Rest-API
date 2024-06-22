from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from author.models import AuthorModel
from author.serializers import AuthorSerializer



class AuthorMainView(APIView):

    def get(self, request):
        author = AuthorModel.objects.all()
        serializer = AuthorSerializer(author, many=True)
        response = {
            'success': True,
            'total': author.count(),
            'author': serializer.data()
        }

        return Response(response, status=status.HTTP_200_OK)