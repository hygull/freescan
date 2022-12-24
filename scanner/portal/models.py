from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False, help_text='Name of the category ex: Property Scan, Pdf Scan etc.')
	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.name} - {"Enabled" if self.active else "Disabled"}'
