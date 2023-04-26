from rest_framework import serializers
from .models import Modification, Cooling, Housing, PowerSupplyUnit, RAM, GraphicsCard, Motherboard, Processor, Memory

from rest_framework import serializers
from .models import Modification

class ModificationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255, default='')
    author_id = serializers.IntegerField()
    likes = serializers.IntegerField(default=0)

    housing = serializers.PrimaryKeyRelatedField(queryset=Housing.objects.all())
    motherboard = serializers.PrimaryKeyRelatedField(queryset=Motherboard.objects.all())
    power_supply = serializers.PrimaryKeyRelatedField(queryset=PowerSupplyUnit.objects.all())
    processor = serializers.PrimaryKeyRelatedField(queryset=Processor.objects.all())
    graphics_card = serializers.PrimaryKeyRelatedField(queryset=GraphicsCard.objects.all())
    ram = serializers.PrimaryKeyRelatedField(queryset=RAM.objects.all())
    memory = serializers.PrimaryKeyRelatedField(queryset=Memory.objects.all())
    cooling = serializers.PrimaryKeyRelatedField(queryset=Cooling.objects.all())

    def validate(self, data):
        # proverka sovmestimosti proccessors and materi
        if not data['processor'].socket == data['motherboard'].socket:
            raise serializers.ValidationError("Processor and motherboard are not compatible.")
        return data

    def create(self, validated_data):
        return Modification.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.housing = validated_data.get('housing', instance.housing)
        instance.motherboard = validated_data.get('motherboard', instance.motherboard)
        instance.power_supply = validated_data.get('power_supply', instance.power_supply)
        instance.processor = validated_data.get('processor', instance.processor)
        instance.graphics_card = validated_data.get('graphics_card', instance.graphics_card)
        instance.ram = validated_data.get('ram', instance.ram)
        instance.memory = validated_data.get('memory', instance.memory)
        instance.cooling = validated_data.get('cooling', instance.cooling)
        instance.save()
        return instance


class ModificationsSerializer(serializers.ModelSerializer):
    is_compatible = serializers.BooleanField(read_only=True)

    class Meta:
        model = Modification
        fields = '__all__'


class CoolingSerializer2(serializers.Serializer):
    TYPE_CHOICES = [
        ('CPU Cooler', 'CPU Cooler'),
        ('Case Fan', 'Case Fan'),
        ('Liquid Cooler', 'Liquid Cooler')
    ]

    type = serializers.ChoiceField(choices=TYPE_CHOICES)
    socket = serializers.CharField(max_length=50)
    maximum_noise_level = serializers.IntegerField()


    def create(self, validated_data):
        return Cooling.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.socket = validated_data.get('socket', instance.socket)
        instance.maximum_noise_level = validated_data.get('maximum_noise_level', instance.maximum_noise_level)

        instance.save()
        return instance


class CoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooling
        fields = '__all__'


class HousingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Housing
        fields = '__all__'


class PowerSupplyUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerSupplyUnit
        fields = '__all__'


class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = "__all__"


class GraphicCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphicsCard
        fields = '__all__'


class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = '__all__'


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = '__all__'


class Memory(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = '__all__'