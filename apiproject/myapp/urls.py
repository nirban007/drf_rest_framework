from django.urls import path
from django.urls.conf import include
from myapp import views
from myapp.views import ContractViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contact', ContractViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = format_suffix_patterns([

#      path('myapi/', views.BlogList.as_view()),
#      path('detail/<int:pk>/', views.ApiDetail.as_view()),
#      path('genaric_api/', views.ContractList.as_view(), name='contract-list'),
#      path('mydetail/<int:pk>/', views.ContractDetail.as_view(), name='contract-list'),
#      path('', views.api_root),

    
# ])