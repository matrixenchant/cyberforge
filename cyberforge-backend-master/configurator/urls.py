from django.urls import path
from .views import *

app_name = 'configurator'
urlpatterns = [
    path('modifications/', ModificationList.as_view(), name='modifications-list'),
    path('modifications/<int:id>/', ModificationDetail.as_view(), name='configurator-detail'),
    path('cooling/', CoolingList.as_view(), name='cooling-list'),
    path('cooling/<int:id>/', CoolingDetail.as_view(), name='cooling-detail'),
    path('housing/', HousingList.as_view(), name='housing-list'),
    path('housing/<int:id>/', HousingDetailF, name='housing-detail'),
    path('power_supply_unit/', PowerSupplyUnitList.as_view(), name='power_supply_unit-list'),
    path('power_supply_unit/<int:id>/', PowerSupplyUnitDetail.as_view(), name='power_supply_unit-detail'),
    path('ram/', RAMList.as_view(), name='ram-list'),
    path('ram/<int:id>/', RAMDetail.as_view(), name='ram-detail'),
    path('gpu/', GPUList.as_view(), name='graphic_card-list'),
    path('gpu/<int:id>/', GPUDetail.as_view(), name='graphic_card-detail'),
    path('motherboard/', MotherboardList.as_view(), name='motherboard-list'),
    path('motherboard/<int:id>/', MotherboardDetail.as_view(), name='motherboard-detail'),
    path('cpu/', CPUList.as_view(), name='processor-list'),
    path('cpu/<int:id>/', CPUDetail.as_view(), name='processor-detail'),
    path('memory/', MemoryList.as_view(), name='memory-list'),
    path('memory/<int:id>/', MemoryDetail.as_view(), name='memory-detail'),
]


