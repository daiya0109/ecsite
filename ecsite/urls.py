from django.contrib import admin
from django.urls import path, include # 追加
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

# 投稿した画像を表示するための設定、解説は 4.3 を参照 
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)