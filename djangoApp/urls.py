
from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
#start rest api framework task
from rest_framework import routers
from restAPI.views import MovieViewSet, ActionTypeMovie, ComedyTypeMovie

router = routers.SimpleRouter()
router.register(r'movies', MovieViewSet)
router.register(r'actions', ActionTypeMovie)
router.register(r'comedy', ComedyTypeMovie)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('movies', include(router.urls)),
    path('', include('food.urls')),
    path('register/',user_view.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html') ,name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'users/logout.html'), name='logout'),
    path('profile', user_view.profile, name='profile'),

]
urlpatterns += router.urls
urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)