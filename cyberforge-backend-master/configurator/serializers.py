from rest_framework import serializers
from rest_framework.fields import SkipField

from .models import Modification, Cooling, Housing, PowerSupplyUnit, RAM, GPU, Motherboard, CPU, Memory, Socket

from rest_framework import serializers
from .models import Modification


class get_spec_ser:
    def get_spec(self, obj):
        spec_data = []
        for label in obj.spec_labels:
            value = getattr(obj, label['slug'], None)
            if value is not None:
                spec_data.append({
                    'slug': label['slug'],
                    'label': label['label'],
                    'value': str(value)
                })

        return spec_data


class SocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socket
        fields = '__all__'


class CoolingSerializer2(serializers.Serializer, get_spec_ser):
    TYPE_CHOICES = [
        ('CPU Cooler', 'CPU Coolertea'),
        ('Case Fan', 'Case Fan'),
        ('Liquid Cooler', 'Liquid Cooler')
    ]
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)
    type = serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    images = serializers.ImageField(required=False, allow_null=True, read_only=True)
    rating = serializers.IntegerField(default=0, min_value=0)

    cooling_type = serializers.ChoiceField(choices=TYPE_CHOICES, write_only=True)
    sockets = SocketSerializer(many=True, write_only=True)
    maximum_noise_level = serializers.IntegerField(write_only=True)

    def get_spec(self, obj):
        spec_data = []
        for label in obj.spec_labels:
            value = getattr(obj, label['slug'], None)
            if value is not None:
                if label['slug'] == 'sockets':
                    serializer = SocketSerializer(value, many=True)
                    value = [item['socket'] for item in serializer.data]
                    value = ", ".join(value)
                spec_data.append({
                    'slug': label['slug'],
                    'label': label['label'],
                    'value': str(value)
                })

        return spec_data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['spec'] = self.get_spec(instance)
        return ret

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


class HousingSerializer(serializers.ModelSerializer, get_spec_ser):
    class Meta:
        model = Housing
        fields = '__all__'
        extra_kwargs = {
            'case_form_factor': {'write_only': True},
            'compatible_board_form_factor': {'write_only': True},
            'dimensions': {'write_only': True},
        }

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['spec'] = self.get_spec(instance)
        return ret


class PowerSupplyUnitSerializer(serializers.ModelSerializer, get_spec_ser):
    class Meta:
        model = PowerSupplyUnit
        fields = '__all__'
        extra_kwargs = {
            'psu_power': {'write_only': True},
            'efficiency': {'write_only': True},
            'form_factor': {'write_only': True},
            'noise_level': {'write_only': True},
        }

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['spec'] = self.get_spec(instance)
        return ret


class RAMSerializer(serializers.ModelSerializer, get_spec_ser):
    class Meta:
        model = RAM
        fields = "__all__"
        extra_kwargs = {
            'memory_type': {'write_only': True},
            'memory_capacity': {'write_only': True},
            'memory_clock_speed': {'write_only': True},
        }

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['spec'] = self.get_spec(instance)
        return ret


class GPUSerializer(serializers.ModelSerializer, get_spec_ser):
    class Meta:
        model = GPU
        fields = '__all__'
        extra_kwargs = {
            'interface': {'write_only': True},
            'video_memory_capacity': {'write_only': True},
            'rated_power': {'write_only': True},
            'video_memory_type': {'write_only': True},
            'technical_process': {'write_only': True},
            'gpu_frequency': {'write_only': True},
            'chipset_model': {'write_only': True},
            'connectors': {'write_only': True},
            'length': {'write_only': True},
        }

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['spec'] = self.get_spec(instance)
        return ret


class MotherboardSerializer(serializers.ModelSerializer, get_spec_ser):
    class Meta:
        model = Motherboard
        fields = '__all__'
        extra_kwargs = {
            'socket': {'write_only': True},
            'form_factor': {'write_only': True},
            'num_memory_slots': {'write_only': True},
            'power_connectors': {'write_only': True},
        }

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['spec'] = self.get_spec(instance)
        return ret


class CPUSerializer(serializers.ModelSerializer, get_spec_ser):
    class Meta:
        model = CPU
        fields = '__all__'
        extra_kwargs = {
            'socket': {'write_only': True},
            'processor_type': {'write_only': True},
            'total_number_of_cores': {'write_only': True},
            'total_number_of_threads': {'write_only': True},
            'clock_frequency': {'write_only': True},
            'process_technology': {'write_only': True},
            'rated_power': {'write_only': True},
        }

    def get_spec(self, obj):
        spec_data = []
        for label in obj.spec_labels:
            value = getattr(obj, label['slug'], None)
            if value is not None:
                if label['slug'] == 'socket':
                    serializer = SocketSerializer(value)
                    value = serializer.data['socket']
                spec_data.append({
                    'slug': label['slug'],
                    'label': label['label'],
                    'value': str(value)
                })

        return spec_data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['spec'] = self.get_spec(instance)
        return ret


class MemorySerializer(serializers.ModelSerializer, get_spec_ser):
    class Meta:
        model = Memory
        fields = '__all__'
        extra_kwargs = {
            'socket': {'write_only': True},
            'processor_type': {'write_only': True},
            'total_number_of_cores': {'write_only': True},
            'total_number_of_threads': {'write_only': True},
            'clock_frequency': {'write_only': True},
            'process_technology': {'write_only': True},
            'rated_power': {'write_only': True},
        }

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['spec'] = self.get_spec(instance)
        return ret


class ModificationGetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255, default='')
    author_name = serializers.CharField(max_length=255)
    likes = serializers.IntegerField(default=0)

    housing = HousingSerializer
    motherboard = MotherboardSerializer
    power_supply = PowerSupplyUnitSerializer
    cpu = CPUSerializer
    gpu = GPUSerializer
    ram = RAMSerializer
    memory = MemorySerializer
    cooling = CoolingSerializer2

    comp = {
        'housing': housing,
        "motherboard": motherboard,
        'power_supply': power_supply,
        'cpu': cpu,
        'gpu': gpu,
        'ram': ram,
        'memory': memory,
        'cooling': cooling
    }

    def get_component(self, obj, comp):
        component_data = []
        for label in obj.components_labels:
            value = getattr(obj, label['slug'], None)
            if value is not None:
                serializer = comp[label['slug']](value)
                value = serializer.data
                component_data.append({
                    'slug': label['slug'],
                    'label': label['label'],
                    'value': value
                })

        return component_data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['components'] = self.get_component(instance, self.comp)
        return ret

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


class ModificationSerializer(serializers.ModelSerializer):
    is_compatible = serializers.BooleanField(read_only=True)
    is_compatible_cooling = serializers.BooleanField(read_only=True)

    class Meta:
        model = Modification
        fields = '__all__'

    def validate(self, data):
        # проверка совместимости процессоров и материнских плат
        if not data['cpu'].socket == data['motherboard'].socket:
            raise serializers.ValidationError("Processor and motherboard are not compatible.")
        elif not data['motherboard'].socket in data['cooling'].sockets.all():
            raise serializers.ValidationError("Motherboard socket and cooling socket are not compatible.")
        return data
