from rest_framework import serializers
from .models import Service, News, GoalAssessment, FAQ, Contact, Certificate, Partner, Numbers, WhenNeedAssessment


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class GoalAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalAssessment
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class NumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = '__all__'


class WhenNeedAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhenNeedAssessment
        fields = '__all__'
