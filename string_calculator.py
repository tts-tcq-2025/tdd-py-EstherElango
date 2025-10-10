# string_calculator.py
import re
from typing import List, Tuple


def parse_input(s: str) -> Tuple[List[str], str]:
    """
    Parse the optional delimiter header and return (delimiters, numbers_string).
    Default delimiters are comma and newline.
    Supports:
      - //;\n1;2    -> delimiter ';'
      - //[***]\n1***2 -> delimiter '***'
      - //[*][%]\n1*2%3 -> multiple delimiters
    """
    if not s:
        return [',', '\n'], ''

    if s.startswith('//'):
        nl = s.find('\n')
        if nl == -1:
            raise ValueError("Invalid input: missing newline after delimiter declaration")
        header = s[2:nl]
        rest = s[nl + 1 :]

        if header.startswith('['):
            # one or more [delim] pieces
            delims = re.findall(r'\[(.*?)\]', header)
            if not delims:
                raise ValueError("Invalid delimiter header")
        else:
            # single char delimiter (e.g. //;\n)
            delims = [header]
        return delims, rest

    return [',', '\n'], s


def split_tokens(numbers_str: str, delimiters: List[str]) -> List[str]:
    """Split numbers_str into tokens using the delimiters list."""
    if numbers_str == '':
        return []
    # build regex pattern joining escaped delimiters
    pattern = '|'.join(re.escape(d) for d in delimiters)
    return re.split(pattern, numbers_str)


def tokens_to_ints(tokens: List[str]) -> List[int]:
    """Convert tokens to ints. Empty token -> ValueError (invalid input)."""
    ints = []
    for t in tokens:
        t = t.strip()
        if t == '':
            raise ValueError("Invalid input: empty number token")
        try:
            n = int(t)
        except ValueError:
            raise ValueError(f"Invalid number token: {t}")
        ints.append(n)
    return ints


def add(numbers: str) -> int:
    """
    Add numbers from the input string according to the rules:
      - empty string => 0
      - default delimiters: comma , and newline \n
      - optional header: //[delim]\n or //[delim1][delim2]\n
      - negative numbers raise ValueError: "negatives not allowed: -1, -2"
      - numbers > 1000 are ignored
    """
    delimiters, numbers_str = parse_input(numbers)
    tokens = split_tokens(numbers_str, delimiters)
    nums = tokens_to_ints(tokens) if tokens else []

    negatives = [n for n in nums if n < 0]
    if negatives:
        negs = ", ".join(str(n) for n in negatives)
        raise ValueError(f"negatives not allowed: {negs}")

    total = sum(n for n in nums if n <= 1000)
    return total
