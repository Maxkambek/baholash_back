from .serializers import GoalAssessmentSerializer, ServiceSerializer, NewsSerializer, FAQSerializer, ContactSerializer, \
    CertificateSerializer, PartnerSerializer, NumbersSerializer, WhenNeedAssessmentSerializer
from .models import Service, News, GoalAssessment, FAQ, Contact, Certificate, Partner, Numbers, WhenNeedAssessment
from rest_framework import generics


class CertificateListAPIView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class PartnerListAPIView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class NumbersListAPIView(generics.ListAPIView):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer


class WhenNeedListAPIView(generics.ListAPIView):
    queryset = WhenNeedAssessment.objects.all()
    serializer_class = WhenNeedAssessmentSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class FAQListAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class GoalListAPIView(generics.ListAPIView):
    queryset = GoalAssessment.objects.all()
    serializer_class = GoalAssessmentSerializer


class GoalDetailListAPIView(generics.ListAPIView):
    queryset = GoalAssessment.objects.all()
    serializer_class = GoalAssessmentSerializer


class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetailListAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
