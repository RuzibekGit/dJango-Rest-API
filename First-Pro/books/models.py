from django.db import models


class BooksModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=254)
    pages = models.IntegerField()
    in_stock = models.BooleanField(default=False)
    content = models.TextField()
    isbn = models.CharField(max_length=25, unique=True)


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
