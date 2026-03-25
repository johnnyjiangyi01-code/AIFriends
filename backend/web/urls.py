from django.contrib.auth.views import PasswordResetView
from django.urls import path, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from web.views.create.character.create import CreateCharacter
from web.views.create.character.get_list import  GetListCharacterView
from web.views.create.character.get_single import GetSingleCharacterView
from web.views.create.character.remove import RemoveCharacter
from web.views.create.character.update import UpdateCharacter
from web.views.friend.get_list import GetListFriendView
from web.views.friend.get_or_create import GetOrCreateFriendView
from web.views.friend.remove import RemoveFriendView
from web.views.homepage.index import HomePageIndexView
from web.views.index import index
from web.views.message.chat.chat import MessageChatView
from web.views.user.account.get_user_info import GetUserInfoView
from web.views.user.account.login import LoginView
from web.views.user.account.logout import LogoutView
from web.views.user.account.refresh_token import RefreshTokenView
from web.views.user.account.register import RegisterView
from web.views.user.profile.update import  UpdateProfileView

urlpatterns = [
    path('api/user/account/login/', LoginView.as_view() ),  # api/用于区分前后端的api
    path('api/user/account/logout/', LogoutView.as_view() ),
    path('api/user/account/register/', RegisterView.as_view() ),
    path('api/user/account/refresh_token/',  RefreshTokenView.as_view() ),
    path('api/user/account/get_user_info/', GetUserInfoView.as_view() ),

    path('api/user/profile/update/', UpdateProfileView.as_view() ),

    path('api/create/character/create/' ,CreateCharacter.as_view() ),
    path('api/create/character/update/', UpdateCharacter.as_view() ),
    path('api/create/character/remove/', RemoveCharacter.as_view() ),
    path('api/create/character/get_single/', GetSingleCharacterView.as_view() ),
    path('api/create/character/get_list/', GetListCharacterView.as_view() ),

    path('api/homepage/index/', HomePageIndexView.as_view() ),

    path('api/friend/get_or_create/',GetOrCreateFriendView.as_view() ),

    path('api/friend/remove/', RemoveFriendView.as_view() ),

    path('api/friend/get_list/', GetListFriendView.as_view() ),

    path('api/friend/message/chat/',MessageChatView.as_view() ),
    path('',index),

    re_path(r'^(?!media/|static/|assets/).*$', index)  #兜底路由，其他的都不匹配就用这个
]

