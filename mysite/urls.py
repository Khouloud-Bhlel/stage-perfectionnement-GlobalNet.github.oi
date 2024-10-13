from django.contrib import admin
from django.urls import path, include
from map import views 
from django.shortcuts import render
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('map.urls')),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('administrator/', administrator),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handle404 = 'map.views.handle404'
