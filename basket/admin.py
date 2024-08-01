from django.contrib import admin
from django.contrib.admin import register
from basket.models import Basket, BasketLine


class BasketLineInline(admin.TabularInline):
    model = BasketLine


@register(BasketLine)
class BasketLine(admin.ModelAdmin):
    list_display = ['basket', 'quantity']


@register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_time']
    inlines = [BasketLineInline]

