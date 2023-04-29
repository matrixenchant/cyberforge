from braces.views import CsrfExemptMixin
from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import *

User = get_user_model()


class PaginationClass(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10

    class Meta:
        ordering = ['-id']


class ModificationList(CsrfExemptMixin, mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    pagination_class = PaginationClass

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ModificationGetSerializer
        return ModificationSerializer

    def get_queryset(self):
        return Modification.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user.username)
        modification = serializer.save()
        user = self.request.user
        user.modifications.add(modification)


class ModificationDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Modification.objects.all()
    serializer_class = ModificationGetSerializer
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ModificationGetSerializer
        return ModificationSerializer

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
        serializer = CoolingSerializer2(cooling, many=True, context={'request': request})
        return Response(serializer.data)
    if request.method == "POST":
        serializer = CoolingSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CoolingList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Cooling.objects.all()
    serializer_class = CoolingSerializer2
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PaginationClass

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CoolingDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Cooling.objects.all()
    serializer_class = CoolingSerializer2
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class HousingList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PaginationClass

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@permission_classes([IsAuthenticatedOrReadOnly])
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
            if not request.data.get('static'):
                serializer.validated_data.pop('static', None)
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
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PowerSupplyUnitList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = PowerSupplyUnit.objects.all()
    serializer_class = PowerSupplyUnitSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PaginationClass

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PowerSupplyUnitDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = PowerSupplyUnit.objects.all()
    serializer_class = PowerSupplyUnitSerializer
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class RAMList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PaginationClass

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RAMDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GPUList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PaginationClass

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GPUDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MotherboardList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PaginationClass

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MotherboardDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CPUList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PaginationClass

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CPUDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MemoryList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PaginationClass

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MemoryDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
