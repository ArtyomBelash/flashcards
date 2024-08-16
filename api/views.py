from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwnerOrAdminOnly
from api.serializers import CardSerializer
from cards.models import Card


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    permission_classes = (IsOwnerOrAdminOnly, IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Card.objects.all()
        if self.request.user.is_authenticated:
            return Card.objects.filter(owner=self.request.user)



