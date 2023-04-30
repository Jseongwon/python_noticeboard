from django.contrib import admin
from django.urls import path
# index는 대문, blog는 게시판
from main.views import index, blog, postingdetail, postinginsert, postingdelete

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', postingdetail, name='postingdetail'),
    path('blog/postinginsert/', postinginsert),
    path('blog/<int:pk>/postingdelete/', postingdelete),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)