from rest_framework import serializers
from .models import AwardsMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = ('name', 'description', 'bio','link','profile_image')