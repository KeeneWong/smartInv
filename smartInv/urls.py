from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('items/', views.ItemList.as_view(), name='item_list'),

    path('items/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),

    path('catergorys/', views.CatergoryList.as_view(), name='catergory_list'),

    path('catergorys/<int:pk>', views.CatergoryDetail.as_view(),
         name='catergory_detail'),

    path('useritems/<str:userid>',
         views.UserItemList.as_view(), name='useritem_list'),

    path('createuser/', views.UserCreateAPIView.as_view(), name='create_user'),
    #     path('users/', views.UserList.as_view(), name='user_list'),
    #     path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
