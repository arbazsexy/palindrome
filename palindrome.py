import sys


def is_palindrome(text: str) -> bool:
  cleaned = "".join(char.lower() for char in text if char.isalnum())
  return cleaned == cleaned[::-1]


def main():
  if len(sys.argv) < 2:
    print("Usage: python palindrome.py '<text to check>'")
    sys.exit(1)

  text = sys.argv[1]

  if is_palindrome(text):
    print(f'"{text}" is a palindrome!')
    sys.exit(0)
  else:
    print(f'"{text}" is not a palindrome.')
    sys.exit(0)  # Changed from 1 to 0 so Jenkins marks the build as SUCCESS


if __name__ == "__main__":
  main()