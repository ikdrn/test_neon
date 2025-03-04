import os
from django.core.wsgi import get_wsgi_application

# 環境変数 "DJANGO_SETTINGS_MODULE" にプロジェクトの設定ファイルを指定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# WSGI アプリケーションを取得し、サーバーに渡す
application = get_wsgi_application()
