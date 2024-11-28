from rest_framework import serializers


class RecommendationRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)