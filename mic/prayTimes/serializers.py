from rest_framework import serializers
from prayTimes.models import PrayTimeTable


class PrayTimeTableSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    monthNum = serializers.IntegerField(default=0)
    image = serializers.ImageField()

    def create(self, validated_data):
        return PrayTimeTable.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.monthNum = validated_data.get('monthNum', instance.monthNum)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
