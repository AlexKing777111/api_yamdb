from django.urls import include, path
from rest_framework import routers

from api.views import ReviewViewSet, CommentViewSet
from . import views

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register(
    r'xxxxxxxxxxxxxx/reviews',
    ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'xxxxxxxxxxxxxxxxxxxx/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]