from rest_framework.routers import DefaultRouter

from polls import views

router = DefaultRouter()

router.register(r'', views.PollViewSet, base_name='polls')

urlpatterns = router.urls
