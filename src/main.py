"""チャットアプリケーションのエントリーポイント。

このモジュールは、チャットアプリケーションを起動するためのエントリーポイントを提供します。
"""

from src.chat_app import ChatApp


def main() -> None:
    """アプリケーションのメイン関数。

    ChatAppインスタンスを作成し、アプリケーションを起動します。
    """
    app = ChatApp()
    # デフォルトでは、http://127.0.0.1:7860 でアプリケーションが起動します
    app.launch(share=False)  # share=Trueにすると、一時的な公開URLが生成されます


if __name__ == "__main__":
    main()
