from django.urls import path
from .views import index, upload_data,CreateItem,getSubCategory,orderslist
urlpatterns = [
    path("", index, name='index_page'),
    path("upload/", upload_data, name='upload_data'),
    path("create/",CreateItem.as_view(),name='create_item'),
    path("get_subs/",getSubCategory,name='get_subs'),
    path("orders_list/",orderslist,name='order_list'),
]
