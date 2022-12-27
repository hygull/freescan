from django.urls import path
from portal.views import DocumentView

urlpatterns = (
	path('scanner/', DocumentView.as_view(), name='scanner_url'),
)
