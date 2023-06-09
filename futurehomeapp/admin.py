from django.contrib import admin
from .models import Listing, Question, Answer
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Listing)
class ListingAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('address',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    list_display = ('address', 'slug', 'status', 'created_on')
    search_fields = ['address', 'content']


@admin.register(Question)
class QuestionAdmin(SummernoteModelAdmin):
    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'listing', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_questions']

    def approve_questions(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Answer)
class AnswerAdmin(SummernoteModelAdmin):
    list_filter = ('created_on',)
    list_display = ('author', 'question', 'created_on')
