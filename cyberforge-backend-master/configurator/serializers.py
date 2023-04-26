from rest_framework import serializers
from .models import Modification, Cooling, Housing, PowerSupplyUnit, RAM, GPU, Motherboard, CPU, Memory, Socket

from rest_framework import serializers
from .models import Modification


class SocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socket
        fields = '__all__'


class CoolingSerializer2(serializers.Serializer):
    TYPE_CHOICES = [
        ('CPU Cooler', 'CPU Cooler'),
        ('Case Fan', 'Case Fan'),
        ('Liquid Cooler', 'Liquid Cooler')
    ]
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)
    producer = serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    images = serializers.ImageField(required=False, allow_null=True, read_only=True)
    performance = serializers.IntegerField(default=0, min_value=0)

    cooling_type = serializers.ChoiceField(choices=TYPE_CHOICES)
    socket = SocketSerializer(many=True)
    maximum_noise_level = serializers.IntegerField()

    def create(self, validated_data):
        sockets_data = validated_data.pop('sockets', [])
        cooling = Cooling.objects.create(**validated_data)
        for socket_data in sockets_data:
            socket, _ = Socket.objects.get_or_create(name=socket_data['name'])
            cooling.sockets.add(socket)
        return cooling

    def update(self, instance, validated_data):
        sockets_data = validated_data.pop('sockets', [])
        instance = super().update(instance, validated_data)
        instance.sockets.clear()
        for socket_data in sockets_data:
            socket, _ = Socket.objects.get_or_create(name=socket_data['name'])
            instance.sockets.add(socket)
        return instance

    def get_images_url(self, obj):
        request = self.context.get('request')
        images = obj.images.all()
        if images:
            return [request.build_absolute_uri(image.image.url) for image in images]
        return []

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


class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = '__all__'


class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = '__all__'


class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = '__all__'


class ModificationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255, default='')
    author_name = serializers.CharField(max_length=255)
    likes = serializers.IntegerField(default=0)

    housing = HousingSerializer()
    motherboard = MotherboardSerializer()
    power_supply = PowerSupplyUnitSerializer()
    cpu = CPUSerializer()
    gpu = GPUSerializer()
    ram = RAMSerializer()
    memory = MemorySerializer()
    cooling = CoolingSerializer2()

    def validate(self, data):
        # proverka sovmestimosti proccessors and materi
        if not data['cpu'].socket == data['motherboard'].socket:
            raise serializers.ValidationError("Processor and motherboard are not compatible.")
        elif not data['motherboard'].socket in data['cooling'].socket:
            raise serializers.ValidationError("Motherboard socket and cooling socket are not compatible.")
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
        instance.cpu = validated_data.get('cpu', instance.cpu)
        instance.gpu = validated_data.get('gpu', instance.gpu)
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
