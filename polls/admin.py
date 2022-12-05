from django.contrib import admin

# Register your models here.
from .models import Question,Choice,Item,Purchase

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Item)
admin.site.register(Purchase)
