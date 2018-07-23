from rest_framework import serializers
from .models import listings,images,users


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = images
        fields = ('image_url',)

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('email','firstname','lastname',)

class ListingsSerializer(serializers.ModelSerializer):

    image_url = serializers.ReadOnlyField(source='image__image_url')      
    user_email = serializers.ReadOnlyField(source='user__email')       
    user_firstname = serializers.ReadOnlyField(source='user__firstname')       
    user_lastname = serializers.ReadOnlyField(source='user__lastname')   
    user_cell = serializers.ReadOnlyField(source='user__cell')       
    

    class Meta:
        model = listings
        fields=('listing_id','title','price','image_url','user_email','user_firstname','user_lastname','user_cell','description')