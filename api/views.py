from .models import listings
from .serializers import ListingsSerializer
from rest_framework import generics


class ListingsCreate(generics.ListCreateAPIView):
    queryset = listings.objects.all().values('listing_id','price','title','description','image','image__image_url','user','user__email','user__firstname','user__lastname','user__cell')
    serializer_class = ListingsSerializer