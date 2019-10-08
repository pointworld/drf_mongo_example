from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from polls import models
from polls import serializers


class PollViewSet(MongoModelViewSet):
    """"""

    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer
    lookup_field = 'name'
