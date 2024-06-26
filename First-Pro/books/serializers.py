from rest_framework import serializers

from books.models import BooksModel



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'

    def get_fields(self):
        # Dynamically customize the fields based on the provided 'fields_data' if exist.
        fields_data = self.context.get('fields_data', [])
        fields = super().get_fields()

        if fields_data:
            fields = {field: fields[field] for field in fields_data}

        return fields
