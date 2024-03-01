from django.contrib import admin
from .models import Service, News, GoalAssessment, FAQ, Contact, Certificate, Partner, Numbers, WhenNeedAssessment

admin.site.register(News)
admin.site.register(FAQ)
# admin.site.register(GoalAssessment)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Certificate)
admin.site.register(Partner)
admin.site.register(Numbers)
admin.site.register(WhenNeedAssessment)
