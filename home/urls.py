from django.urls import path, include
from .import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage),
    path('sale', views.sale),
    path('man', views.man),
    path('women', views.women),
    path('home', views.homepage),
    path('about_us', views.about_us),
    path('View/<int:id>/', views.View),
    path('sign_in', views.sign_in),
    path('sign_up', views.sign_up),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)