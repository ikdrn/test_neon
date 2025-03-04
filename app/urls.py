from django.urls import path
from .views import login_view, success_view

# アプリ内のURLパターンを定義
urlpatterns = [
    # ルートパス ('') にアクセスすると login_view を実行（名前: 'login'）
    path('', login_view, name='login'),
    # 'success/' にアクセスすると success_view を実行（名前: 'success'）
    path('success/', success_view, name='success'),
]
