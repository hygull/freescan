from django.db import models


class Category(models.Model):
	"""
	A model which represents a Database table with information needed for a Category.

	Fields
	------
	name : str
		Name of the category

	active : bool
		Status of the category 

	created_at : datetime
		Created date of the category

	updated_at : bool
		Updated date of the category  
	"""
	
	name = models.CharField(max_length=100, null=False, blank=False, help_text='Name of the category ex: Property Scan, Pdf Scan etc.')
	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.name} {"(Enabled)" if self.active else "(Disabled)"}'

	class Meta:
		verbose_name_plural = 'Categories'
