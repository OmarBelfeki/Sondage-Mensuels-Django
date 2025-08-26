from django.contrib import admin
from .models import Participant, Reponse, Sondage, Question

admin.site.register(Participant)
admin.site.register(Reponse)
admin.site.register(Sondage)
admin.site.register(Question)
