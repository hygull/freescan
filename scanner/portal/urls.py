from django.urls import path
from portal.views import LoginView

urlpatterns = (
	path('scanner/', LoginView.as_view(), name='login_url'),
)
