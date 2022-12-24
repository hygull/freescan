from django.contrib import admin
from portal.models import Category


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'active', 'created_at', 'updated_at']
	search_fields = ['name', 'active']

admin.site.register(Category, CategoryAdmin)