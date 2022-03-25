from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView

from apps.members import views as member_views
from apps.members import api as member_api
from apps.landing_page import views as landing_page_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page_views.LandingPageView.as_view(), name="landing-page"),
    path('contact-form/', landing_page_views.contact_view, name="contact-form"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('add-car/', member_views.AddCarView.as_view(), name="add-car"),
    path('api/cars/', member_api.CarApiView.as_view(), name="api-get-cars"),
    path("monitoring/", include("django_prometheus.urls")),
]
