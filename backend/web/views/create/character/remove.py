from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from web.models.character import Character
from web.views.utils.photo import remove_old_photo


class RemoveCharacter(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            character_id = request.data['character_id']
            character = Character.objects.get(pk=character_id ,author__user = request.user)
            remove_old_photo(character.photo)
            remove_old_photo(character.background_image)
            character.delete()

            return Response({
                'result': 'success',
            })
        except:
            return Response({
                'result':'系统异常请稍后重试'
            })