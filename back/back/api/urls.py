
from django.urls import path
from api import views

# Example
urlpatterns = [
     path('userpc/', views.UserPCListApiView.as_view()),
     path('userpc/<int:pk>/', views.UserPCDetailApiView.as_view()),
     path('cpu/', views.CPUListApiView.as_view()),
     path('cpu/<int:pk>/', views.CPUDetailApiView.as_view()),
     path('videocard/', views.VideoCardListApiView.as_view()),
     path('videocard/<int:pk>/', views.VideoCardDetailApiView.as_view()),
     path('motherboard/', views.MotherboardListApiView.as_view()),
     path('motherboard/<int:pk>/', views.MotherboardDetailApiView.as_view()),
     path('ram/', views.RAMListApiView.as_view()),
     path('ram/<int:pk>/', views.RAMDetailApiView.as_view()),
     path('memory/', views.MemoryListApiView.as_view()),
     path('memory/<int:pk>/', views.MemoryDetailApiView.as_view()),
     path('cooling/', views.CoolingListApiView.as_view()),
     path('cooling/<int:pk>/', views.CoolingDetailApiView.as_view()),
     path('corpus/', views.CorpusListApiView.as_view()),
     path('corpus/<int:pk>/', views.CorpusDetailApiView.as_view()),
     path('powerunit/', views.PowerUnitListApiView.as_view()),
     path('powerunit/<int:pk>/', views.PowerUnitDetailApiView.as_view()),
]
