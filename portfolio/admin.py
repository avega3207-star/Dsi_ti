from django.contrib import admin
from .models import portfolio

@admin.register(portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    readonly_fields = ['created', 'updated']