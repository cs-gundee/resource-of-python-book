from prime import is_prime

def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"Алдаа!!! is_prime({n}) ба төлөвлөсөн үр дүн {expected}")