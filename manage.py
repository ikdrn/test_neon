#!/usr/bin/env python
# このスクリプトは Django のコマンドラインツールを起動するためのエントリーポイントです。

import os  # OS（オペレーティングシステム）に依存した機能を利用するためのモジュール
import sys  # Python インタプリタとの対話に必要なモジュール

def main():
    # 環境変数 "DJANGO_SETTINGS_MODULE" にプロジェクトの設定ファイルを指定する
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    
    try:
        # Django のコマンドラインユーティリティをインポート
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Django がインストールされていない場合、エラーメッセージを出力して例外を発生させる
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and available on your PYTHONPATH."
        ) from exc
    # コマンドライン引数に基づいて適切なコマンドを実行
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # このスクリプトが直接実行された場合に main() を呼び出す
    main()
