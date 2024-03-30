

from .views import process_img
from django .urls import path

urlpatterns = [
    path('process_img/', process_img, name="process_img")

]