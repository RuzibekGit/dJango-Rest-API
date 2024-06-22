from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from books.models import BooksModel
from books.serializers import BookSerializer


# -------------------- Get All Books ----------------------
# region get all
@api_view(['GET'])
def get_data_books(request, *args, **kwargs):
    books = BooksModel.objects.all()
    data = BookSerializer(
        books, 
        many=True, 
        context={'fields_data': ['id', 'title', 'author', 'pages']}
        ).data

    return Response(data)
#endregion

# -------------------- Get Detail -------------------------
# region detail
@api_view(['GET'])
def get_book(request, pk, *args, **kwargs):
    try:
        book = BooksModel.objects.get(id=pk)
        return Response(BookSerializer(book).data)
    
    except BooksModel.DoesNotExist:
        return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    
# endregion


# -------------------- Update ----------------------------
# region update
@api_view(['PUT', 'PATCH'])
def update_book(request, pk, *args, **kwargs):
    try:
        serializer = BookSerializer(
            BooksModel.objects.get(id=pk), 
            data=request.data, 
            partial=request.method == 'PATCH'
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except BooksModel.DoesNotExist:
        return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

# endregion

# -------------------- Create -------------------------
# region create
@api_view(['POST'])
def create_book(request, *args, **kwargs):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# endregion


# -------------------- Delete -------------------------
# region delete
@api_view(['DELETE'])
def delete_book(request, pk, *args, **kwargs):
    try:
        BooksModel.objects.get(id=pk).delete()
        return Response({'message': 'Book deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    except BooksModel.DoesNotExist:
        return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

# endregion


# -------------------- Filter By Page ----------------------
# region filter
@api_view(['GET'])
def filter_by_books(request, *args, **kwargs):
    books = BooksModel.objects.all().order_by('-pages')
    data = BookSerializer(
        books,
        many=True,
        context={'fields_data': ['pages',  'title', 'id' ]}
    ).data

    return Response(data)
# endregion


# -------------------- * ----------------------
# region *


# endregion
