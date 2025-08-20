import random

def play_game():
    """
    1から100までのランダムな数字を当てる数当てゲームを実行します。
    """
    # 1から100までのランダムな整数を生成
    answer = random.randint(1, 100)
    attempts = 0

    print("数当てゲームへようこそ！")
    print("1から100までの数字を1つ予想して入力してください。")

    while True:
        try:
            # ユーザーからの入力を受け取る
            guess_str = input("あなたの予想: ")
            guess = int(guess_str)
            attempts += 1

            # 入力された数値が範囲内かチェック
            if guess < 1 or guess > 100:
                print("エラー: 1から100までの数字を入力してください。")
                continue

            # 予想と答えを比較
            if guess < answer:
                print("もっと大きい数字です！")
            elif guess > answer:
                print("もっと小さい数字です！")
            else:
                print(f"\nおめでとうございます！正解です！")
                print(f"答えは {answer} でした。")
                print(f"あなたは {attempts} 回で正解しました。")
                break
        except ValueError:
            print("エラー: 有効な数値を入力してください。")

if __name__ == "__main__":
    while True:
        play_game()

        # もう一度プレイするか確認
        play_again = input("\nもう一度プレイしますか？ (yes / no): ").lower().strip()
        if play_again not in ["yes", "y", "はい"]:
            print("遊んでくれてありがとうございました！")
            break
        print("\n" + "="*30)