"""相槌パターンの管理と生成を担当するモジュール。

このモジュールは、ユーザー入力に対する相槌パターンを管理し、
ランダムに選択して返す機能を提供します。
"""

import random
from typing import List


class ResponseGenerator:
    """相槌パターンの管理と生成を担当するクラス。

    このクラスは、複数の相槌パターンを保持し、ユーザー入力に対して
    ランダムに選択した相槌を返す機能を提供します。

    Attributes:
        response_patterns (List[str]): 相槌パターンのリスト
    """

    def __init__(self) -> None:
        """ResponseGeneratorクラスのコンストラクタ。

        相槌パターンを初期化します。
        """
        self.response_patterns: List[str] = [
            "なるほど、それは興味深いですね。",
            "確かに、その通りだと思います。",
            "そうなんですね、理解できました。",
            "面白い視点ですね。",
            "それについてもっと教えてください。",
            "素晴らしい考えですね。",
            "そうですか、それは知りませんでした。",
            "なるほど、参考になります。",
            "それは良いアイデアですね。",
            "確かに、そう考えると納得できます。"
        ]

    def generate_response(self, user_input: str) -> str:
        """ユーザー入力に対する相槌を生成します。

        Args:
            user_input (str): ユーザーが入力したテキスト

        Returns:
            str: ランダムに選択された相槌
        """
        # 現在はユーザー入力の内容に関わらず、ランダムに相槌を返す
        # 将来的には、ユーザー入力の内容に応じた相槌を返すように拡張可能
        return random.choice(self.response_patterns)
