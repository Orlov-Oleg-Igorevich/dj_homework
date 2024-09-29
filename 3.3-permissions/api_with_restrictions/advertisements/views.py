from django.db.models import F
from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import permissions
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer

class F(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator']

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = F
    ordering_fields = ['created_at', ]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == 'list':
            return [permissions.AllowAny()]
        elif self.action in ["create", "retrieve"]:
            return [permissions.IsAuthenticated()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated(), IsOwner()]
        return [permissions.AllowAny()]
