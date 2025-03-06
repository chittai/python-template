"""Gradioを使用したチャットアプリケーションのメインモジュール。

このモジュールは、Gradioを使用してチャットインターフェースを構築し、
ユーザーとの対話を可能にします。
"""

from typing import List, Tuple

import gradio as gr

from src.response_generator import ResponseGenerator


class ChatApp:
    """チャットアプリケーションのメインクラス。

    このクラスは、Gradioインターフェースの構築と実行を担当します。

    Attributes:
        response_generator (ResponseGenerator): 応答生成を担当するオブジェクト
        interface (gr.Interface): Gradioインターフェースオブジェクト
    """

    def __init__(self) -> None:
        """ChatAppクラスのコンストラクタ。

        ResponseGeneratorを初期化し、Gradioインターフェースを構築します。
        """
        self.response_generator = ResponseGenerator()
        self.interface = self.build_interface()

    def build_interface(self) -> gr.Blocks:
        """Gradioインターフェースを構築します。

        Returns:
            gr.Blocks: 構築されたGradioインターフェース
        """
        with gr.Blocks(title="シンプルチャットアプリ") as interface:
            gr.Markdown("# シンプルチャットアプリ")
            gr.Markdown("メッセージを入力して会話を始めましょう。")

            chatbot = gr.Chatbot(height=400)
            msg = gr.Textbox(
                placeholder="ここにメッセージを入力してください...",
                container=False,
                scale=7
            )
            submit_btn = gr.Button("送信", scale=1)

            def respond(message: str, chat_history: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[str, str]]]:
                """ユーザー入力に対する応答を生成します。

                Args:
                    message (str): ユーザーが入力したメッセージ
                    chat_history (List[Tuple[str, str]]): チャット履歴

                Returns:
                    Tuple[str, List[Tuple[str, str]]]: 空の入力フィールドと更新されたチャット履歴
                """
                if not message.strip():
                    return "", chat_history

                # ResponseGeneratorを使用して応答を生成
                bot_response = self.response_generator.generate_response(message)
                
                # チャット履歴に追加
                chat_history.append((message, bot_response))
                
                return "", chat_history

            # イベントの設定
            submit_btn.click(
                respond,
                inputs=[msg, chatbot],
                outputs=[msg, chatbot]
            )
            msg.submit(
                respond,
                inputs=[msg, chatbot],
                outputs=[msg, chatbot]
            )

            # クリアボタンの追加
            clear_btn = gr.Button("履歴をクリア")
            clear_btn.click(lambda: None, None, chatbot, queue=False)

        return interface

    def launch(self, **kwargs) -> None:
        """アプリケーションを起動します。

        Args:
            **kwargs: gr.launch()に渡す追加のパラメータ
        """
        self.interface.launch(**kwargs)
