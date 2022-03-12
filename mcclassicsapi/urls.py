from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_token_views
from django.urls import path, include
from mcclassicsapi import views


router = DefaultRouter(trailing_slash=False)
router.register(r'comments', views.CommentsView, 'comments')
router.register(r'help', views.HelpView, 'help')
router.register(r'projects', views.ProjectsView, 'projects')
router.register(r'events', views.EventView, 'events')
router.register(r'profiles', views.ProfileView, 'profiles')


urlpatterns = [
    path('', include(router.urls)),
    path('login', auth_token_views.obtain_auth_token),
    path('register', views.register_user)
]
