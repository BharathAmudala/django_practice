from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StockViewSet, PurchaseViewSet, SaleViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'stock', StockViewSet)
router.register(r'purchase', PurchaseViewSet)
router.register(r'sale', SaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]