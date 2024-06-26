from django.shortcuts import render

from rest_framework import  generics

from books.models import BooksModel
from books.serializers import BookSerializer




# -------------------- Get All Books ----------------------
# region get all
class GetAllBooks(generics.ListAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer

#endregion


# -------------------- Get Detail -------------------------
# region detail
class BookDetailView(generics.RetrieveAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer

# endregion


# -------------------- Update ----------------------------
# region update
class UpdateBookView(generics.UpdateAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer

# endregion


# -------------------- Create ----------------------------
# region create
class CreateBookView(generics.CreateAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer

# endregion


# -------------------- Delete ----------------------------
# region delete
class DeleteBookView(generics.DestroyAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer

# endregion


# -------------------- All view in One ---------------------
# region all for one
class BookView(generics.GenericAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer
# endregion

