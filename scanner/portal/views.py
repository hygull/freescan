from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic.base import View
from portal.models import Category
import PyPDF2


class LoginView(View):
	def get(self, request, *args, **kwargs):
		categories = Category.objects.filter(active=True)

		context = {
			'categories': categories
		}
		return render(request, 'index.html', context)


class DocumentView(APIView):
	def get(request, *args, **kwargs):
		file = open('docs/sample.pdf', 'rb')
		pdf_reader = PyPDF2.PdfReader(file)
		pdf_reader.pages[0].extract_text()

		return Response({
			'status': 200, 
			'message': 'Document is processed successfully'
		})