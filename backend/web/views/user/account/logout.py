from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated #只有是登录状态才能logout

class LogoutView(APIView):
    permission_classes = [IsAuthenticated] #强制必须登录才能访问 否则返回401
    def post(self,request):
        response = Response({
            'result': 'success',
        })
        response.delete_cookie('refresh_token')
        return response