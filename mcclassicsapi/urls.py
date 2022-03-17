from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf.urls.static import static
from mcclassics import settings
from mcclassicsapi import views


router = DefaultRouter(trailing_slash=False)
router.register(r'comments', views.CommentsView, 'comments')
router.register(r'help', views.HelpView, 'help')
router.register(r'projects', views.ProjectsView, 'projects')
router.register(r'events', views.EventView, 'events')
router.register(r'profiles', views.ProfileView, 'profiles')


urlpatterns = [
    path('', include(router.urls)),
    path('login', views.login_user),
    path('register', views.register_user)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)