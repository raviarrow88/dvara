from django.urls import path
from .views import index, upload_data
urlpatterns = [
    path("", index, name='index_page'),
    path("upload/", upload_data, name='upload_data'),
]
