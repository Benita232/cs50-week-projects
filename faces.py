def convert(str):
    """Convert emoticons to emojis using a translation dictionary"""
    emoticon_map = {":)": "🙂", ":(": "🙁"}
    for emoticon, emoji in emoticon_map.items():
        str = str.replace(emoticon, emoji)
    return str

def main():
    """Handle user input and output without explicit prompt"""
    print(convert(input()))

if __name__ == "__main__":
    main()


