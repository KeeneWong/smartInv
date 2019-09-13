from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('items/', views.ItemList.as_view(), name='item_list'),
    path('items/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
    path('catergorys/', views.CatergoryList.as_view(), name='catergory_list'),
    path('catergorys/<int:pk>', views.CatergoryDetail.as_view(),
         name='catergory_detail'),
    # path('useritems/', views.UserItemList.as_view(), name='useritem_list')
    path('useritems/<str:userid>',
         views.UserItemList.as_view(), name='useritem_list'),
    path('users2/', views.UserViewSet2.as_view(), name='user_list'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
