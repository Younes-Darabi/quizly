from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.quizzes.api.views import QuizzesView


router = DefaultRouter()
router.register(r'quizzes', QuizzesView, basename='quizzes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.authentication.api.urls')),
    path('api/', include(router.urls))
]