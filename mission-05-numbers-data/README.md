# Mission 5 — Numbers and Data

## 1. Task / objective
Practise manual conversions between decimal, binary, and hexadecimal number systems; verify every result using Python's built-in functions; build and test a Python `number_converter.py` program; and explain how computers store text using character encodings like ASCII and UTF-8.

## 2. Work completed

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| --- | --- |
| Convert decimal `13` to binary | Divide repeatedly by 2 and read remainders bottom-up: `13 ÷ 2 = 6 r 1`, `6 ÷ 2 = 3 r 0`, `3 ÷ 2 = 1 r 1`, `1 ÷ 2 = 0 r 1` -> **`1101`** (check: `8 + 4 + 0 + 1 = 13`). |
| Convert decimal `25` to binary | Divide repeatedly by 2: `25 ÷ 2 = 12 r 1`, `12 ÷ 2 = 6 r 0`, `6 ÷ 2 = 3 r 0`, `3 ÷ 2 = 1 r 1`, `1 ÷ 2 = 0 r 1` -> **`11001`** (check: `16 + 8 + 0 + 0 + 1 = 25`). |
| Convert binary `1010` to decimal | Multiply each bit by its power of 2: `(1 × 2^3) + (0 × 2^2) + (1 × 2^1) + (0 × 2^0) = 8 + 0 + 2 + 0` -> **`10`**. |
| Convert binary `1101` to decimal | `(1 × 2^3) + (1 × 2^2) + (0 × 2^1) + (1 × 2^0) = 8 + 4 + 0 + 1` -> **`13`**. |
| Convert hexadecimal `A` to decimal | In base 16, digits `A–F` represent `10–15`; `A × 16^0 = 10 × 1` -> **`10`**. |
| Convert hexadecimal `1F` to decimal | `(1 × 16^1) + (15 × 16^0) = 16 + 15` -> **`31`**. |
| Convert binary `1111` to hexadecimal | Convert binary `1111` to decimal first: `8 + 4 + 2 + 1 = 15`. In base 16, `15` is represented by **`F`**. |

---

### Task 5.2 — Verify using Python

| Manual task | Python expression tested | Python result | Matches manual answer? |
| --- | --- | --- | --- |
| Decimal `13` -> binary | `bin(13)` | `'0b1101'` | Yes (`1101`) |
| Decimal `25` -> binary | `bin(25)` | `'0b11001'` | Yes (`11001`) |
| Binary `1010` -> decimal | `int('1010', 2)` | `10` | Yes (`10`) |
| Binary `1101` -> decimal | `int('1101', 2)` | `13` | Yes (`13`) |
| Hexadecimal `A` -> decimal | `int('A', 16)` | `10` | Yes (`10`) |
| Hexadecimal `1F` -> decimal | `int('1F', 16)` | `31` | Yes (`31`) |
| Binary `1111` -> hexadecimal | `hex(int('1111', 2))` | `'0xf'` | Yes (`F`) |

---

### Task 5.3 — Build a small number converter
Built [number_converter.py](number_converter.py) inside `mission-05-numbers-data/`.
- **How it works:**
  1. Uses `input()` to read a decimal number from the user as text.
  2. Converts that text into a Python integer with `int()` (and catches `ValueError` if non-numeric text is entered).
  3. Converts the integer to binary using `bin()` and to hexadecimal using `hex()`.
  4. Prints both the prefixed Python format (`0b...`, `0x...`) and the clean digits without prefixes.
- **What `bin()` and `hex()` do:**
  - `bin(n)` takes an integer and returns its base-2 string representation prefixed with `0b` to clearly indicate binary.
  - `hex(n)` takes an integer and returns its base-16 string representation prefixed with `0x` to clearly indicate hexadecimal.

**Test runs from Terminal (`python3 number_converter.py`):**

| Test number | Binary output | Hexadecimal output |
| --- | --- | --- |
| `13` | `0b1101` (`1101`) | `0xd` (`D`) |
| `25` | `0b11001` (`11001`) | `0x19` (`19`) |
| `42` | `0b101010` (`101010`) | `0x2a` (`2A`) |
| `255` | `0b11111111` (`11111111`) | `0xff` (`FF`) |

---

### Task 5.4 — How is text stored?
- **ASCII decimal codes (verified with Python `ord()`):**
  - Uppercase `A` -> **`65`** (`ord('A') == 65`)
  - Lowercase `a` -> **`97`** (`ord('a') == 97`)
- **Why a computer needs an encoding standard to store text:**
  At the hardware level, computers can only store binary numbers (`0`s and `1`s), not letters directly. An encoding standard like ASCII or UTF-8 defines an agreed-upon mapping between characters and numeric codes so that any computer or program reads and displays the exact same text.
- **Example of a character not part of basic ASCII:**
  The Indian Rupee symbol **`₹`** (Unicode `U+20B9`), Hindi letters like **`अ`**, or emojis like **`😀`** are outside the 128-character basic ASCII table and require an encoding such as UTF-8.

## 3. Commands / tools used
- `python3` interactive shell — Verified every manual conversion and checked ASCII codes.
- `input()`, `int()`, `bin()`, `hex()`, `ord()` — Python built-in functions used to read user input, convert bases, and inspect character codes.
- `python3 number_converter.py` — Ran the converter script from Terminal with four test numbers (`13`, `25`, `42`, `255`).
- `git add` & `git commit` — Staged and committed the converter script, README, and test output evidence.

## 4. My understanding
Everything inside a computer—numbers, text, and instructions—ultimately boils down to bits (`0` and `1`). Binary matches hardware on/off states directly, while hexadecimal is a compact shorthand because every 4 bits equals exactly one hex digit (for instance, `1111` = `F` and `11111111` = `FF`). Character encodings like ASCII and UTF-8 extend that same numeric foundation to text, allowing computers worldwide to store English letters, currency symbols, regional scripts, and emojis reliably.

## 5. Difficulties faced
Remembering that `bin()` and `hex()` include the `0b` and `0x` prefixes—and that `input()` always returns a string (`str`) rather than an integer—meant forgetting `int()` would cause a `TypeError`.

## 6. How I resolved them
Wrapped `input()` with `int()` inside a `try/except ValueError` block so non-integer inputs produce a helpful message instead of crashing, and displayed both the raw `0b`/`0x` form and the clean prefix-free digits.

## 7. Evidence / files
- [mission-05-numbers-data/number_converter.py](number_converter.py) — Working interactive Python number converter.
- [mission-05-numbers-data/README.md](README.md) — Manual working, Python verification table, converter test table, and text-encoding answers.
- [evidence/mission-05-converter-output.txt](../evidence/mission-05-converter-output.txt) — Recorded Python verification and converter test outputs.

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Push status:** Committed on `main` (staged and committed separately from Mission 4; ready to push to GitHub).
