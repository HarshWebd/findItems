from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('insertPage',views.insertPage,name='insertPage'),
    path('insertItem',views.insertItems,name='insertItems'),
    path('showItem',views.ShowItems,name='ShowItems'),
]



from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)