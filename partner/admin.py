'''
from django.contrib import admin
from django.contrib.admin import register
from partner.models import Partner, PartnerStock


@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']


@register(PartnerStock)
class PartnerStock(admin.ModelAdmin):
    list_display = ['partner', 'product', 'price']
    search_fields = ['partner']
'''