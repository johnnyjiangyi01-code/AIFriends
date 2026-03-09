from django.contrib.auth.views import PasswordResetView
from django.urls import path, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from web.views.index import index
from web.views.user.account.get_user_info import GetUserInfoView
from web.views.user.account.login import LoginView
from web.views.user.account.logout import LogoutView
from web.views.user.account.refresh_token import RefreshTokenView
from web.views.user.account.register import RegisterView

urlpatterns = [
    path('api/user/account/login/', LoginView.as_view() ),  # api/用于区分前后端的api
    path('api/user/account/logout/', LogoutView.as_view() ),
    path('api/user/account/register/', RegisterView.as_view() ),
    path('api/user/account/refresh_token/',  RefreshTokenView.as_view() ),
    path('api/user/account/get_user_info/', GetUserInfoView.as_view() ),
    path('',index),

    re_path(r'^(?!media/|static/|assets/).*$', index)  #兜底路由，其他的都不匹配就用这个
]

