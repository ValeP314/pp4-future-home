from django.contrib import admin
from .models import Listing, Feature
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Listing)
class ListingAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('address',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    list_display = ('address', 'slug', 'status', 'created_on')
    search_fields = ['address', 'content']


@admin.register(Feature)
class FeatureAdmin(SummernoteModelAdmin):

    list_filter = ('price', 'ber_category')
    list_display = ('listing', 'status')
    search_fields = ['listing', 'content']
