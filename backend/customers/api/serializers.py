from rest_framework import serializers
from ..models import Customer
from ..choices import GENDER_CHOICES

"""
In the given Django REST Framework (DRF) CustomerSerializer class, there's a method called get_created(self, obj). This method is used to customize the serialization of the created field of the Customer model.

Here's how it works and why it's used:

Purpose:
The purpose of the get_created method is to customize the representation of the created field when it's serialized into JSON or any other format by the serializer. By default, when DRF serializes a DateTimeField, it will use its default string representation, which might not always be in the desired format. The get_created method allows you to customize this representation.

SerializerMethodField:
In the serializer class, the created field is defined as a SerializerMethodField. This field type allows you to include custom logic to determine the value of the field during serialization. Instead of directly mapping to a model field, a SerializerMethodField calls a custom method to get the value for the field.

Method Signature:
The get_created method takes two parameters: self and obj.

self: This is a reference to the serializer instance and allows you to access other attributes or methods within the serializer.
obj: This parameter represents the individual object being serialized. In this case, it represents an instance of the Customer model.
Custom Logic:
Inside the get_created method, the logic converts the created datetime field into a string representation using the strftime method with a specific format ("%Y-%m-%d %H:%M:%S"). This format represents the date and time in the format "YYYY-MM-DD HH:MM:SS".

Usage:
By defining the get_created method and setting it as the source for the created field in the serializer, you ensure that when the Customer object is serialized, the created field will be represented in the desired format specified in the get_created method.

Overall, the get_created method allows you to customize the serialization behavior of the created field, ensuring that it's represented in a specific format when the Customer objects are serialized using the serializer.
"""
class GenderChoiceFieldSerializer(serializers.Field):
    def to_representation(self, obj):
        return dict(GENDER_CHOICES)[obj]

    def to_internal_value(self, data):
        return data

class CustomerSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()
    gender = GenderChoiceFieldSerializer() # converts 0 and 1 to its choice value using to_representation
    class Meta:
        model = Customer
        fields = "__all__"

    def get_created(self, obj):
        return obj.created.strftime("%Y-%m-%d %H:%M:%S")



