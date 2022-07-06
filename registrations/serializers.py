from django.contrib.auth import get_user_model
from rest_framework import serializers
from registrations.models import Doctor, Donor, Patient
from django.contrib.auth.models import User

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
        # fields = ['username', 'email', 'is_doctor']


class DoctorSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):
        user = User(
            username=self.validated_data["username"],
            email=self.validated_data["email"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({'error': 'Password did not match'})
        user.set_password(password)
        user.is_doctor = True
        user.save()
        Doctor.objects.create(user=user)
        return user


class DonorSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data["username"],
            email=self.validated_data["email"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({'error': 'Password did not match'})
        user.set_password(password)
        user.is_donor = True
        user.save()
        Donor.objects.create(user=user)
        return user


class PatientSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data["username"],
            email=self.validated_data["email"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({'error': 'Password did not match'})
        user.set_password(password)
        user.is_patient = True
        user.save()
        Patient.objects.create(user=user)
        return user
