from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mysite.views import HomeView, lessons_list, card_detail, AboutView, adminka, admin_login_page, check_admin_password, delete_card, delete_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('AboutPage', AboutView.as_view(), name='about'),
    path('PageLearn/', lessons_list, name='PageLearn'),
    path('detail/<int:pk>/', card_detail, name='detail'),
    path('adminka-login/', admin_login_page, name='admin_login'),
    path('admin-login/check/', check_admin_password, name='check_admin_password'),
    path('adminka/', adminka, name='adminka'),
    path('adminka/delete/<int:pk>/', delete_card, name='delete_card'),
    path('adminka/delete_user/<int:user_id>/', delete_user, name='delete_user'),

    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
