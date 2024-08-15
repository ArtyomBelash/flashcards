from rest_framework import serializers

from cards.models import Card


class CardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Card
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user
        return Card.objects.create(**validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if instance.owner == request.user:
            instance.answer = validated_data.get('answer', instance.answer)
            instance.question = validated_data.get('question', instance.question)
            instance.box = validated_data.get('box', instance.box)
            instance.save()
        return instance
