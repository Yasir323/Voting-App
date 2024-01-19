from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Voting App Admin"
admin.site.site_title = "Voting App Admin Area"
admin.site.index_title = "Welcome to the Voting App"


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']}), ('Date Information', {
        'fields': ['published_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
