from dataclasses import fields
from random import choices
from django.contrib import admin

from polls.models import Choice, Question

# Register your models here.


class ChoiceInlines(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Information", {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["published_date"]}),
    ]

    inlines = [ChoiceInlines]
    
    list_display = ("question_text", "published_date", "was_published_recently")

    list_filter = ["published_date"]

    search_fields = ['question_text']
    list_per_page  = 2


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
