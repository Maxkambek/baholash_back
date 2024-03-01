from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsListAPIView.as_view()),
    path('when-need/', views.WhenNeedListAPIView.as_view()),
    path('contact/', views.ContactCreateAPIView.as_view()),
    path('certificate/', views.CertificateListAPIView.as_view()),
    path('partner/', views.PartnerListAPIView.as_view()),
    path('numbers/', views.NumbersListAPIView.as_view()),
    path('faq/', views.FAQListAPIView.as_view()),
    path('goals/', views.GoalListAPIView.as_view()),
    path('goals/<int:pk>/', views.GoalDetailListAPIView.as_view()),
    path('services/', views.ServiceListAPIView.as_view()),
    path('services/<int:pk>/', views.ServiceDetailListAPIView.as_view()),
]
