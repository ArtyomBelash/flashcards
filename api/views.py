from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.permissions import IsOwnerOrAdminOnly
from api.serializers import CardSerializer
from cards.models import Card


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    permission_classes = (IsOwnerOrAdminOnly, IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Card.objects.filter(owner=self.request.user)


