from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from rest_framework import routers
from apps.users.views import UsersViewSet
from apps.posts.views import MovieViewSet, CategoryViewSet, CommentViewSet, LikeViewSet, LikeCommentsViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'Likes', LikeViewSet)
router.register(r'Like_comments', LikeCommentsViewSet)

api_urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('posts/', include('apps.posts.urls')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('api/', include(router.urls)),
    path('',RedirectView.as_view(url='/api/')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

