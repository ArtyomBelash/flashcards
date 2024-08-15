from django.contrib import admin
from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('question', 'owner')
    search_fields = ('id', 'question')
    list_filter = ('question',)
    empty_value_display = 'N/A'
