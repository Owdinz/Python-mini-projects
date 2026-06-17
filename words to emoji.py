#library sys for system module
import sys
#needs to reconfigure the standard output to use UTF-8 encoding to properly display emojis in the console
sys.stdout.reconfigure(encoding='utf-8')
#words and emoji accordingly
emoji_dict={
    "good":"😀",
    "happy":"😊",
    "perfect":"👌",
    "smile":"😄",
    "joy":"😂",
    "star":"⭐",
    "heart":"❤️",
    "love":"❤️",
    "in-love":"😍",
    "fun":"😎",
    "cool":"😎",
    "sad":"😢",
    "broken":"💔",
    "confused":"😕",
    "approve":"👍",
    "approved":"✅",
}
running = True

while running:
    #section for choosing if text to emoji or emoji to text
    print("\nChoose an option:")
    print("1. Text to Emoji")
    print("2. Emoji to Text")
    print("3. Exit")

    #user's choice
    choice = input("Enter your choice (1 , 2 or 3): ").strip()

    convert_words = []

    if choice == "1":  #text to emoji     1
        convert_words = []
        user_input = input("Enter a text to convert to emoji: ").lower().strip()
        words = user_input.split()
        for word in words:  #read and translate per words
            if word in emoji_dict:
                convert_words.append(emoji_dict[word])
            else:
                convert_words.append(word)
        result = " ".join(convert_words)
        print(result)
    elif choice == "3":
        print("Thanks for using the emoji converter! Goodbye!")
        break
    elif choice == "2":  #emoji to text     2
        convert_words = []
        user_input = input("Enter an emoji to convert to text: ").strip()
        emojis = user_input.split()
        found_any = False
        for single_emj in emojis:
            found = False
            for word, emj in emoji_dict.items():
                if emj == single_emj:
                    convert_words.append(word)
                    found = True
                    found_any = True
            if not found:
                convert_words.append(single_emj)
        if not found_any:
            print(f"'{user_input}' not found in the emoji dictionary/library")
        #option 3
        result = " ".join(convert_words)
        print(result)
    elif choice == "3":
        print("Thanks for using the emoji converter! Goodbye!")
        break
    else:
        print("out of bounds!") #once user enter/choose 3 it will end here DON'T change
        break
