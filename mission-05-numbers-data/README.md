# Mission 5 — Numbers and Data

## 1. Task / objective
Convert numbers between decimal, binary, and hexadecimal by hand, verify my answers using Python, build a small number converter program, and understand how computers store text.

## 2. Work completed

### Task 5.1 — Manual conversions
I did each conversion on paper first, showing my working:

| Question | My working | Answer |
| --- | --- | --- |
| Decimal 13 → binary | 13÷2=6 r1, 6÷2=3 r0, 3÷2=1 r1, 1÷2=0 r1 → read remainders bottom-up | `1101` |
| Decimal 25 → binary | 25÷2=12 r1, 12÷2=6 r0, 6÷2=3 r0, 3÷2=1 r1, 1÷2=0 r1 | `11001` |
| Binary 1010 → decimal | (1×8) + (0×4) + (1×2) + (0×1) = 8+0+2+0 | `10` |
| Binary 1101 → decimal | (1×8) + (1×4) + (0×2) + (1×1) = 8+4+0+1 | `13` |
| Hex A → decimal | A = 10 in hex, so 10×1 | `10` |
| Hex 1F → decimal | (1×16) + (15×1) = 16+15 | `31` |
| Binary 1111 → hex | 1111 = 8+4+2+1 = 15, and 15 in hex is F | `F` |

### Task 5.2 — Verifying with Python
I opened the Python shell and checked every answer:

| What I calculated | Python expression | Python result | Match? |
| --- | --- | --- | --- |
| 13 → binary 1101 | `bin(13)` | `0b1101` | ✓ |
| 25 → binary 11001 | `bin(25)` | `0b11001` | ✓ |
| 1010 → decimal 10 | `int('1010', 2)` | `10` | ✓ |
| 1101 → decimal 13 | `int('1101', 2)` | `13` | ✓ |
| A → decimal 10 | `int('A', 16)` | `10` | ✓ |
| 1F → decimal 31 | `int('1F', 16)` | `31` | ✓ |
| 1111 → hex F | `hex(int('1111', 2))` | `0xf` | ✓ |

All matched! The `0b` and `0x` prefixes just tell Python "this is binary" or "this is hex."

### Task 5.3 — Building the number converter
I wrote `number_converter.py` that:
1. Asks the user to type a decimal number
2. Converts it to binary using `bin()` and hexadecimal using `hex()`
3. Shows both the Python format (with `0b`/`0x` prefixes) and clean digits without prefixes

I wrapped the input in `try/except` so it doesn't crash if someone types letters instead of a number.

**Test runs:**

| Input | Binary | Hexadecimal |
| --- | --- | --- |
| 13 | `0b1101` (1101) | `0xd` (D) |
| 25 | `0b11001` (11001) | `0x19` (19) |
| 42 | `0b101010` (101010) | `0x2a` (2A) |
| 255 | `0b11111111` (11111111) | `0xff` (FF) |

The 255 one was satisfying — eight 1s in binary and FF in hex. Makes sense because 255 is the max value for a single byte (8 bits all turned on).

### Task 5.4 — How text is stored
- **ASCII codes:** Uppercase `A` is 65, lowercase `a` is 97 (checked with `ord('A')` and `ord('a')` in Python)
- **Why we need encoding standards:** Computers only understand numbers at the hardware level. Without an agreed-upon mapping (like "65 means A"), different computers would display different characters for the same number. That would be chaos.
- **Character not in basic ASCII:** The Indian Rupee symbol `₹` and Hindi letters like `अ` aren't in the 128-character ASCII table. For those, you need UTF-8, which extends the system to handle pretty much every writing system and emoji.

## 3. Commands / tools used
- Python interactive shell for verification (`bin()`, `hex()`, `int()`, `ord()`)
- `python3 number_converter.py` — ran the converter with 4 test inputs
- `input()`, `int()`, `bin()`, `hex()` — Python built-in functions used in the converter

## 4. My understanding
Everything in a computer comes down to 0s and 1s. Binary maps directly to the hardware (each bit is basically a tiny switch that's either off or on). Hexadecimal is just a shorthand that makes binary easier for humans to read — every 4 bits maps to exactly one hex digit, so `11111111` becomes the much shorter `FF`. And text? Same idea — every character gets a number, and that number gets stored in binary. It's numbers all the way down.

## 5. Difficulties faced
I kept forgetting that `bin()` and `hex()` return strings with prefixes (`0b` and `0x`), and that `input()` always returns a string — so I'd get a `TypeError` if I forgot to wrap it with `int()`.

## 6. How I resolved them
Added `int()` around the input and also wrapped it in a `try/except ValueError` block so if someone types nonsense, they get a helpful message instead of a crash. For the prefixes, I displayed both the raw Python format and a cleaned-up version.

## 7. Evidence / files
- [number_converter.py](number_converter.py) — The working Python converter
- [evidence/mission-05-converter-output.txt](../evidence/mission-05-converter-output.txt) — Python verification and converter test outputs

## 8. Commit details
- **Message:** `Build number converter and practise data representation`
- Committed on `main` and pushed to GitHub.
