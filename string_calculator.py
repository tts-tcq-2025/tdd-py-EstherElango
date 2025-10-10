# string_calculator.py
import re
from typing import List, Tuple


def extract_header_and_body(s: str) -> Tuple[str, str]:
    """Split header and numbers section."""
    if not s.startswith('//'):
        return '', s
    nl = s.find('\n')
    if nl == -1:
        raise ValueError("Invalid input: missing newline after delimiter declaration")
    return s[2:nl], s[nl + 1:]


def get_delimiters(header: str) -> List[str]:
    """Extract delimiters from header or return default delimiters."""
    if not header:
        return [',', '\n']
    if header.startswith('['):
        delims = re.findall(r'\[(.*?)\]', header)
        if not delims:
            raise ValueError("Invalid delimiter header")
        return delims
    return [header]


def parse_input(s: str) -> Tuple[List[str], str]:
    """Return (delimiters, numbers_string)."""
    header, body = extract_header_and_body(s)
    return get_delimiters(header), body


def split_tokens(numbers_str: str, delimiters: List[str]) -> List[str]:
    """Split numbers_str into tokens using the delimiters list."""
    if numbers_str == '':
        return []
    pattern = '|'.join(re.escape(d) for d in delimiters)
    return re.split(pattern, numbers_str)


def token_to_int(t: str) -> int:
    """Convert a single token to integer."""
    t = t.strip()
    if not t:
        raise ValueError("Invalid input: empty number token")
    try:
        return int(t)
    except ValueError:
        raise ValueError(f"Invalid number token: {t}")


def tokens_to_ints(tokens: List[str]) -> List[int]:
    return [token_to_int(t) for t in tokens]


def check_for_negatives(nums: List[int]):
    negatives = [n for n in nums if n < 0]
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")


def add(numbers: str) -> int:
    """Main add function (keeps CCN <= 3)."""
    delims, nums_str = parse_input(numbers)
    tokens = split_tokens(nums_str, delims)
    if not tokens:
        return 0
    nums = tokens_to_ints(tokens)
    check_for_negatives(nums)
    return sum(n for n in nums if n <= 1000)
