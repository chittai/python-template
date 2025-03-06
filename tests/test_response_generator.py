"""ResponseGeneratorクラスのテストモジュール。

このモジュールは、ResponseGeneratorクラスの機能をテストします。
"""

import pytest

from src.response_generator import ResponseGenerator


class TestResponseGenerator:
    """ResponseGeneratorクラスのテストクラス。"""

    def test_init(self) -> None:
        """初期化が正しく行われることをテストします。"""
        generator = ResponseGenerator()
        assert hasattr(generator, 'response_patterns')
        assert isinstance(generator.response_patterns, list)
        assert len(generator.response_patterns) > 0
        assert all(isinstance(pattern, str) for pattern in generator.response_patterns)

    def test_generate_response(self) -> None:
        """応答生成が正しく行われることをテストします。"""
        generator = ResponseGenerator()
        user_input = "こんにちは"
        response = generator.generate_response(user_input)
        
        # 応答が文字列であることを確認
        assert isinstance(response, str)
        
        # 応答が空でないことを確認
        assert response
        
        # 応答がresponse_patternsのいずれかであることを確認
        assert response in generator.response_patterns

    def test_generate_response_with_empty_input(self) -> None:
        """空の入力に対しても応答が生成されることをテストします。"""
        generator = ResponseGenerator()
        user_input = ""
        response = generator.generate_response(user_input)
        
        # 空の入力でも応答が生成されることを確認
        assert isinstance(response, str)
        assert response
        assert response in generator.response_patterns

    def test_response_patterns_not_modified(self) -> None:
        """応答パターンが外部から変更されないことをテストします。"""
        generator = ResponseGenerator()
        original_patterns = generator.response_patterns.copy()
        
        # 応答を生成
        generator.generate_response("テスト")
        
        # パターンが変更されていないことを確認
        assert generator.response_patterns == original_patterns
