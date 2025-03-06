"""テストを実行するためのスクリプト。

このスクリプトは、pytestを使用してテストを実行します。
"""

import sys
import unittest
from unittest.mock import MagicMock, patch

# ResponseGeneratorのテスト
sys.path.append('.')
from src.response_generator import ResponseGenerator

class TestResponseGenerator(unittest.TestCase):
    """ResponseGeneratorクラスのテストクラス。"""

    def test_init(self) -> None:
        """初期化が正しく行われることをテストします。"""
        generator = ResponseGenerator()
        self.assertTrue(hasattr(generator, 'response_patterns'))
        self.assertIsInstance(generator.response_patterns, list)
        self.assertTrue(len(generator.response_patterns) > 0)
        self.assertTrue(all(isinstance(pattern, str) for pattern in generator.response_patterns))

    def test_generate_response(self) -> None:
        """応答生成が正しく行われることをテストします。"""
        generator = ResponseGenerator()
        user_input = "こんにちは"
        response = generator.generate_response(user_input)
        
        # 応答が文字列であることを確認
        self.assertIsInstance(response, str)
        
        # 応答が空でないことを確認
        self.assertTrue(response)
        
        # 応答がresponse_patternsのいずれかであることを確認
        self.assertIn(response, generator.response_patterns)

    def test_generate_response_with_empty_input(self) -> None:
        """空の入力に対しても応答が生成されることをテストします。"""
        generator = ResponseGenerator()
        user_input = ""
        response = generator.generate_response(user_input)
        
        # 空の入力でも応答が生成されることを確認
        self.assertIsInstance(response, str)
        self.assertTrue(response)
        self.assertIn(response, generator.response_patterns)

    def test_response_patterns_not_modified(self) -> None:
        """応答パターンが外部から変更されないことをテストします。"""
        generator = ResponseGenerator()
        original_patterns = generator.response_patterns.copy()
        
        # 応答を生成
        generator.generate_response("テスト")
        
        # パターンが変更されていないことを確認
        self.assertEqual(generator.response_patterns, original_patterns)


# ChatAppのテストはGradioに依存するため、簡易的なテストのみ実行
# 実際のテストでは、Gradioのコンポーネントをモックする必要があります
try:
    import gradio as gr
    from src.chat_app import ChatApp
    
    class TestChatApp(unittest.TestCase):
        """ChatAppクラスの簡易的なテスト。"""
        
        def test_init(self) -> None:
            """初期化が正しく行われることをテストします。"""
            with patch('src.chat_app.ResponseGenerator') as mock_generator:
                with patch('src.chat_app.ChatApp.build_interface') as mock_build:
                    # モックオブジェクトを設定
                    mock_generator.return_value = MagicMock()
                    mock_build.return_value = MagicMock()
                    
                    # ChatAppインスタンスを作成
                    app = ChatApp()
                    
                    # 属性が正しく設定されていることを確認
                    self.assertTrue(hasattr(app, 'response_generator'))
                    self.assertTrue(hasattr(app, 'interface'))
except ImportError:
    print("Gradioモジュールが見つからないため、ChatAppのテストをスキップします。")


if __name__ == '__main__':
    unittest.main(verbosity=2)
