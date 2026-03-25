from django.contrib import admin
from .models import Hospital, EpisodioUrgencia, Triagem, Consulta, Prescricao

admin.site.register(Hospital)
admin.site.register(EpisodioUrgencia)
admin.site.register(Triagem)
admin.site.register(Consulta)
admin.site.register(Prescricao)