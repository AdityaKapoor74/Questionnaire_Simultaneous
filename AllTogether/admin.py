from django.contrib import admin
from .models import *
# Register your models here.

#User Details
admin.site.register(UserDetails)

#Quiz part
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuestionFeatures)
admin.site.register(ChoiceFeatures)
admin.site.register(UserResponses)
admin.site.register(UserResponsesForFeatures)
admin.site.register(Stimuli)
admin.site.register(UserResponsesForDescription)
