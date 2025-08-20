def greet(name: str) -> str:
    """
    指定された名前に対して日本語の挨拶を生成します。

    Args:
        name (str): 挨拶に含める名前。

    Returns:
        str: フォーマットされた日本語の挨拶文字列。
    """
    return f"こんにちは、{name}さん！"

def add(a: int, b: int) -> int:
    """
    2つの数値を足し合わせます。

    Args:
        a (int): 1つ目の数値。
        b (int): 2つ目の数値。

    Returns:
        int: 2つの数値の合計。
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """
    2つの数値の引き算をします。

    Args:
        a (int): 引かれる数。
        b (int): 引く数。

    Returns:
        int: aからbを引いた差。
    """
    return a - b

print(greet("しょうた"))
print(f"1 + 2 = {add(1, 2)}")
print(f"5 - 3 = {subtract(5, 3)}")