import unittest
from unittest.mock import patch
import io
import sys

# テスト対象の関数をインポート
from number_guessing_game import play_game

class TestNumberGuessingGame(unittest.TestCase):
    """
    数当てゲームの play_game 関数のテストスイート。
    """

    def setUp(self):
        """各テストの前に標準出力をキャプチャする準備をします。"""
        self.held_stdout = sys.stdout
        sys.stdout = self.captured_output = io.StringIO()

    def tearDown(self):
        """各テストの後に標準出力を元に戻します。"""
        sys.stdout = self.held_stdout

    @patch('random.randint')
    @patch('builtins.input')
    def test_successful_game_flow(self, mock_input, mock_randint):
        """
        ゲームが正常に進行し、正解して終了するケースをテストします。
        - 予想: 大きい -> 小さい -> 正解
        """
        # モックの設定
        mock_randint.return_value = 50  # 正解の数字を50に固定
        mock_input.side_effect = ['80', '30', '50']  # ユーザー入力をシミュレート

        # テスト対象の関数を実行
        play_game()

        # 出力結果を検証
        output = self.captured_output.getvalue()
        self.assertIn("もっと小さい数字です！", output)
        self.assertIn("もっと大きい数字です！", output)
        self.assertIn("おめでとうございます！正解です！", output)
        self.assertIn("答えは 50 でした。", output)
        self.assertIn("あなたは 3 回で正解しました。", output)

    @patch('random.randint')
    @patch('builtins.input')
    def test_invalid_non_numeric_input(self, mock_input, mock_randint):
        """
        ユーザーが数値以外の無効な値を入力するケースをテストします。
        """
        # モックの設定
        mock_randint.return_value = 25
        mock_input.side_effect = ['abc', '25'] # 無効な入力 -> 正しい入力

        play_game()

        # 出力結果を検証
        output = self.captured_output.getvalue()
        self.assertIn("エラー: 有効な数値を入力してください。", output)
        self.assertIn("おめでとうございます！正解です！", output)
        # 無効な入力ではattemptsはカウントされないため、1回となる
        self.assertIn("あなたは 1 回で正解しました。", output)

    @patch('random.randint')
    @patch('builtins.input')
    def test_out_of_range_input(self, mock_input, mock_randint):
        """
        ユーザーが1から100の範囲外の数値を入力するケースをテストします。
        """
        # モックの設定
        mock_randint.return_value = 75
        mock_input.side_effect = ['0', '101', '75'] # 範囲外 -> 範囲外 -> 正しい入力

        play_game()

        # 出力結果を検証
        output = self.captured_output.getvalue()
        # 範囲外エラーが2回表示されることを確認
        self.assertEqual(output.count("エラー: 1から100までの数字を入力してください。"), 2)
        self.assertIn("おめでとうございます！正解です！", output)
        # 範囲外の入力でもattemptsはカウントされるため、3回となる
        self.assertIn("あなたは 3 回で正解しました。", output)

if __name__ == '__main__':
    unittest.main()