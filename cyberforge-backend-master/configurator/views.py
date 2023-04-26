from rest_framework import generics, mixins, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Modification
from .serializers import *


class ModificationList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Modification.objects.all()
    serializer_class = ModificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)


class ModificationDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Modification.objects.all()
    serializer_class = ModificationsSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(['GET', 'POST'])
def CoolingListF(request):
    if request.method == "GET":
        cooling = Cooling.objects.all()
        serializer = CoolingSerializer2(cooling, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = CoolingSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CoolingList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Cooling.objects.all()
    serializer_class = CoolingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CoolingDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Cooling.objects.all()
    serializer_class = CoolingSerializer2
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class HousingList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@api_view(['GET', 'PUT', 'DELETE'])
def HousingDetailF(request, id):
    try:
        housing = Housing.objects.filter(id=id).get()
    except Housing.DoesNotExist:
        return Response({'message': 'Housing with this ID is not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = HousingSerializer(housing)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = HousingSerializer(housing, data=request.data)
        if serializer.is_valid():
            if not request.data.get('images'):
                serializer.validated_data.pop('images', None)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        housing.delete()
        return Response({'message': 'Housing item was deleted succesfully!'})


class HousingDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PowerSupplyUnitList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = PowerSupplyUnit.objects.all()
    serializer_class = PowerSupplyUnitSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PowerSupplyUnitDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = PowerSupplyUnit.objects.all()
    serializer_class = PowerSupplyUnitSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class RAMList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RAMDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GraphicsCardList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = GraphicsCard.objects.all()
    serializer_class = GraphicCardSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GraphicsCardDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = GraphicsCard.objects.all()
    serializer_class = GraphicCardSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MotherboardList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MotherboardDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProcessorList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProcessorDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
