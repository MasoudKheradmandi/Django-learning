from django.urls import path , include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter


app_name="api-v1"

router = DefaultRouter()
router.register(r'post',views.PostViewSet,basename='post')
urlpatterns = router.urls


# urlpatterns = [
#     # path('post/',views.PostList.as_view(),name='api-list-view'),
#     # path('post/<int:id>/',views.PostDetail.as_view(),name='Detailview'),
# ]


