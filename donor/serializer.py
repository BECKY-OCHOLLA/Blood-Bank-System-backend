from dataclasses import fields
from rest_framework import serializers
from registrations.models import Donor,BloodDonate

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ('user', 'profile_pic', 'mobile')


class BloodDonateSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodDonate
        fields=('donor','disease','age','bloodgroup','unit','status','date')