from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from . import views 

# 1. Тилге көз каранды болбогон шилтемелер (Админка жана Тил которгуч)
# Бул жерде /i18n/ жолу сөзсүз болушу керек, антпесе баскычтар иштебейт.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')), # Тилди которуу функциясы
]

# 2. Тил префикстери менен иштеген шилтемелер (/ky/, /ru/, /en/, /zh-hans/)
urlpatterns += i18n_patterns(
    path('', views.index, name='index'),  # Башкы бет
    path('product/<int:pk>/', views.product_detail, name='product_detail'), # Товардын деталдуу баракчасы
)

# 3. Сүрөттөр жана статикалык файлдар иштеши үчүн (DEBUG=True учурунда)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)