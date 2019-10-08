from rest_framework_mongoengine import serializers

from polls import models


class PollSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.Poll
        fields = '__all__'
