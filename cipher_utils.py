import math

# VALID_CH: list[str] = ['\t', '\n'] + [chr(i) for i in range(32, 127)]
VALID_CH: list[str] = [chr(i) for i in range(ord('A'), ord('Z')+1)] + [chr(i) for i in range(ord('a'), ord('z')+1)] + [',', '.', ';', '("', '")', '(\'', '\')', '%', 'b/', '\\n']
NUM_VALID = len(VALID_CH)


def is_valid_char(ch: str) -> bool:
    return ch in VALID_CH


def get_code(ch: str) -> int:
    '''
    Returns
    -------
    Code equivalent of the char.
    Returns -1 if ch in not a valid char.
    '''
    if ch in VALID_CH:
        return VALID_CH.index(ch)
    return -1


def get_char(code: int) -> str:
    '''
    Returns
    -------
    Char equivalent of the code.
    Returns null char if not a valid code.
    '''
    if code < 0 or code >= len(VALID_CH):
        return '\0'
    return VALID_CH[code]


def modulo_mul_inverse(x: int, m: int) -> int:
    '''
    Returns
    -------
    Returns (1/x) mod m.
    '''
    if x == 0:
        raise ArithmeticError("Inverse is not defined if determinant is zero.")
    if math.gcd(x, m) != 1:
        raise ArithmeticError("Modular inverse for this key is not defined.")
    inv = 1
    while inv < m and (x * inv) % m != 1:
        inv += 1
    return inv
