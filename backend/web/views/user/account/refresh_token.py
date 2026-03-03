#用refresh去刷新access
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class RefreshTokenView(APIView):
    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({
                    'result': 'refresh token不存在',
                }, status=401)  # 必须加401
            refresh = RefreshToken(refresh_token) #自动检验refresh token是不是在有效期内 如果过期报异常

            #没过期
            if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']: #如果ROTATE_REFRESH_TOKENS为true ，每次用refresh刷新access时候也会生成新的refresh ，7天内如果登录过，有效期会延长七天
                refresh.set_jti()
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token),
                })
                response.set_cookie(  # 把refresh放到cookie
                    key='refresh_token',
                    value=str(refresh),
                    httponly=True,
                    samesite='Lax',
                    secure=True,
                    max_age=86400 * 7,
                )
                return response
            return Response({
                'result': 'success',
                'access': str(refresh.access_token),
            })
        except:
            return Response({
                'result': 'refresh token 过期了',
            }, status=401) #必须加401