from Lexer import Lexer

def print_tokens(source: str) -> None:
    print(f"Input: {source!r}")
    tokens = Lexer(source).scan_tokens()
    for t in tokens:
        print(f"  {t.type.name:<18} {t.literal!r}")
    print()

print_tokens("2 + 3")
print_tokens("12 + 345 - 6")
print_tokens("(1 + 2) * 3")
print_tokens("10/2")
print_tokens("1+2-3*4/5")
print_tokens("(((9)))")
print_tokens("")
print_tokens("2 & 3")