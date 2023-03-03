from rest_framework.routers import DefaultRouter

from .views import PostViewSet, LikeViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("likes", LikeViewSet, basename="likes")

urlpatterns = router.urls
