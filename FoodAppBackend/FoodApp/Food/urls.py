from django.urls import path, include
from .views import (
    RestaurantListCreateAPIView,
    RestaurantRetrieveUpdateDestroyAPIView,
    MenuListCreateAPIView,
    MenuRetrieveUpdateDestroyAPIView,
    OrderListCreateAPIView,
    OrderRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView,
    ReviewRetrieveUpdateDestroyAPIView, UserListAPIView
)

from oauth2_provider.views import TokenView, TokenRefreshView, RevokeTokenView

urlpatterns = [
    path('restaurants/', RestaurantListCreateAPIView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantRetrieveUpdateDestroyAPIView.as_view(), name='restaurant-detail'),
    path('menus/', MenuListCreateAPIView.as_view(), name='menu-list'),
    path('menus/<int:pk>/', MenuRetrieveUpdateDestroyAPIView.as_view(), name='menu-detail'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),
    path('users/', UserListAPIView.as_view(), name='user-list'),


    path('oauth2/token/', TokenView.as_view(), name='token'),
    path('oauth2/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('oauth2/token/revoke/', RevokeTokenView.as_view(), name='token_revoke'),
]
