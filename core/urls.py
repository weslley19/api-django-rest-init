from django.urls import path, include
from rest_framework import routers
from .views import BooksViewSet


router = routers.DefaultRouter()
router.register(r'livros', BooksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
