from django.urls import path
from . import views

urlpatterns = [
    # The root path '' now points to our portfolio home page
    path('', views.portfolio_home, name='portfolio_home'),
]