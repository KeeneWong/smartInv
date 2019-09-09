from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('items/', views.ItemList.as_view(), name='item_list'),
    path('items/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
    path('catergorys/', views.CatergoryList.as_view(), name='catergory_list'),
    path('catergorys/<int:pk>', views.CatergoryDetail.as_view(),
         name='catergory_detail'),
    # path('useritems/', views.UserItemList.as_view(), name='useritem_list')
    path('useritems/<int:userid>',
         views.UserItemList.as_view(), name='useritem_list')
]
