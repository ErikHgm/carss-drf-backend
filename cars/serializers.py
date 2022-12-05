from rest_framework import serializers
from .models import Car
from saved.models import Save


class CarSerializer(serializers.ModelSerializer):
    """ Car Serializer """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    save_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, car=obj
            ).first()
            return save.id if save else None
        return None

    class Meta:
        model = Car
        fields = '__all__'
