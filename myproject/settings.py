import os
from pathlib import Path  # ファイルシステムのパス操作を容易にするモジュール
import dj_database_url  # 環境変数からデータベース設定を読み込むためのモジュール

# プロジェクトのルートディレクトリを取得（settings.py の2階層上）
BASE_DIR = Path(__file__).resolve().parent.parent

# セキュリティ上の秘密鍵（本番環境では適切に管理してください）
SECRET_KEY = 'your-secret-key'  # 本番環境では適切な値に変更してください

# DEBUG モード（本番では False に設定する必要があります）
DEBUG = True

# このプロジェクトで許可するホスト（必要に応じて変更してください）
ALLOWED_HOSTS = []

# インストール済みアプリケーションのリスト
INSTALLED_APPS = [
    'django.contrib.admin',          # 管理サイト機能
    'django.contrib.auth',           # 認証システム
    'django.contrib.contenttypes',   # コンテンツ型システム
    'django.contrib.sessions',       # セッション管理
    'django.contrib.messages',       # メッセージフレームワーク
    'django.contrib.staticfiles',    # 静的ファイル管理
    'app',                           # 独自アプリケーション（ここでは "app" を追加）
]

# ミドルウェアの設定（リクエスト/レスポンス処理のフック）
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF対策
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ルートURLconfの指定（URLルーティングの設定ファイル）
ROOT_URLCONF = 'myproject.urls'

# テンプレートの設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # テンプレートエンジンの指定
        'DIRS': [ BASE_DIR / 'app' / 'templates' ],  # カスタムテンプレートのディレクトリ
        'APP_DIRS': True,  # アプリケーション内のテンプレートディレクトリも検索
        'OPTIONS': {
            'context_processors': [  # テンプレートに渡すコンテキストの設定
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI アプリケーションのパス
WSGI_APPLICATION = 'myproject.wsgi.application'

# NEON_CONNECT 環境変数からDB接続情報を取得
NEON_CONNECT = os.environ.get('NEON_CONNECT')
if not NEON_CONNECT:
    raise Exception("NEON_CONNECT environment variable is not set")

# データベースの設定（dj_database_url を利用して環境変数からパース）
DATABASES = {
    'default': dj_database_url.parse(NEON_CONNECT)
}

# パスワードのバリデーション（セキュリティ向上のための標準設定）
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 国際化の設定
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True  # 国際化対応
USE_TZ = True    # タイムゾーン対応

# 静的ファイルの設定
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'  # collectstatic コマンドで集められるディレクトリ
