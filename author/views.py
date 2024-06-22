from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from author.models import AuthorModel
from author.serializers import AuthorSerializer




# -------------------- List, Detail ----------------------------
# region main view
class AuthorMainView(APIView):
    def get(self, request, pk=None):
        if pk: # agar url tomonidan pk berilgan bo'lsa(:8000/user/2/) detail qismi ishlaydi va return orqli algorithm yakunlanadi
            author = AuthorModel.objects.filter(id=pk).first()
            if author:
                serializer = AuthorSerializer(author)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
            
        # else:
        authors = AuthorModel.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        
        response_data = {
            'success': True,
            'total': authors.count(),
            'authors': serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
# endregion



# -------------------- Create ----------------------------
# region create
class AuthorCreateView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# endregion



# -------------------- Update ----------------------------
# region update
class AuthorUpdateView(APIView):

    def put_patch(self, request, pk, method):
        try:
            author = AuthorModel.objects.get(id=pk)
            serializer = AuthorSerializer(author, data=request.data, partial=method)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except AuthorModel.DoesNotExist:
            return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
    def put(self, request, pk):
        return self.put_patch(request, pk, False)
        
    def patch(self, request, pk):
        return self.put_patch(request, pk, True)

# endregion



# -------------------- Delete ----------------------------
# region delete
class AuthorDeleteView(APIView):
    def delete(self, request, pk):
        try:
            author = AuthorModel.objects.get(id=pk)
            name = author.first_name
            author.delete()
            return Response({'message': f"{name}`s data is deleted! "}, status=status.HTTP_204_NO_CONTENT)
        except AuthorModel.DoesNotExist:
            return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
# endregion