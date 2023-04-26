from django.urls import path
from .views import *

app_name = 'configurator'
urlpatterns = [
    path('modifications/', ModificationList.as_view(), name='modifications-list'),
    path('modifications/<int:id>/', ModificationDetail.as_view(), name='configurator-detail'),
    path('cooling/', CoolingListF, name='cooling-list'),
    path('cooling/<int:id>/', CoolingDetail.as_view(), name='cooling-detail'),
    path('housing/', HousingList.as_view(), name='housing-list'),
    path('housing/<int:id>/', HousingDetailF, name='housing-detail'),
    path('power_supply_unit/', PowerSupplyUnitList.as_view(), name='power_supply_unit-list'),
    path('power_supply_unit/<int:id>/', PowerSupplyUnitDetail.as_view(), name='power_supply_unit-detail'),
    path('ram/', RAMList.as_view(), name='ram-list'),
    path('ram/<int:id>/', RAMDetail.as_view(), name='ram-detail'),
    path('graphic_card/', GraphicsCardList.as_view(), name='graphic_card-list'),
    path('graphic_card/<int:id>/', GraphicsCardDetail.as_view(), name='graphic_card-detail'),
    path('motherboard/', MotherboardList.as_view(), name='motherboard-list'),
    path('motherboard/<int:id>/', MotherboardDetail.as_view(), name='motherboard-detail'),
    path('processor/', ProcessorList.as_view(), name='processor-list'),
    path('processor/<int:id>/', ProcessorDetail.as_view(), name='processor-detail'),
]


