from django.urls import path
from . import views
from .views import ServiceListView,ServiceCreateView
from django.shortcuts import render
from .views import service_list
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.conf.urls.static import static


def is_admin_with_password(user):
    return user.is_authenticated and user.username == 'admin' and user.check_password('123')

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(is_admin_with_password)
def administrator(request):
    # Your view logic here
    return render(request, 'admin_index.html')



from django.urls import path
from .views import upload_files

urlpatterns = [
 #  path('index', views.index, name='index'),
    path('', views.service_and_map, name='service_and_map'),
   # path('services/', ServiceListView.as_view(), name='service_list'),
    path('services/', views.service_list, name='service_list'),
   # path('services/add/', ServiceCreateView.as_view(), name='service_create'),
    path('services/add/', views.service_add, name='service_add'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('services/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('gestion_en_ligne/', views.gestion_en_ligne, name='gestion_en_ligne'),
    path('success/', views.success, name='success'),
            path('delete/<int:client_id>/', views.delete_client, name='delete_client'),
    path('simple/', views.simple, name='simple'),
    path('data/', views.data, name='data'),
    path('administrator/', administrator),

    path('home/', views.service_and_map, name='service_and_map'),
    path('client/delete/<int:pk>/', views.client_delete, name='client_delete'),
    path('search/', service_list, name='search_services'),
path('display_map/', views.display_map, name='display_map'),
path('upload/', upload_files, name='upload_files'),
path('drag/',views.drag,name='drag')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

