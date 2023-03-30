from rest_framework import serializers

from electronics.models import Contact, TradeNetwork


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class TradeNetworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradeNetwork
        fields = '__all__'


    def update(self, instance, validated_data):
        if instance.arrears != validated_data.get("debt"):
            raise serializers.ValidationError("Нельзя обновить задолженность")
        return super().update(instance, validated_data)