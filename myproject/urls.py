from django.contrib import admin
from django.urls import path, include

# ルートURLパターンの定義
urlpatterns = [
    path('admin/', admin.site.urls),  # 管理サイトへのルーティング
    path('', include('app.urls')),      # ルートパスはアプリ "app" の urls.py に委譲
]
