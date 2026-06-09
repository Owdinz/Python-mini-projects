#library sys for system module
import sys
#needs to reconfigure the standard output to use UTF-8 encoding to properly display emojis in the console
sys.stdout.reconfigure(encoding='utf-8')
#for the emoji library
import emoji

#words and emoji accordingly
emoji_dict={
    "good":"😀",
    "happy":"😊",
    "perfect":"👌",
    "smile":"😄",
    "joy":"😂",
    "star":"⭐",
    "heart":"❤️",
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

#users choice
    choice = input("Enter your choice (1 or 2): ").strip()

    convert_words = []
#option 1
    if choice == "1": #outer condition
        user_input = input("Enter a text to convert to emoji: ").lower().strip()
        words = user_input.split()
        for word in words: #read and translate per words
            if word in emoji_dict:
                convert_words.append(emoji_dict[word])
                
            else:
                print(f"'{word}'""word is not found in the emoji dictionary/library, please try again.")
                convert_words.append(word)
#option 2
    elif choice == "2": #outer condition
        user_input = input("Enter an emoji to convert to text: ").strip()
        emojis = user_input.split()
        for single_emj in emojis:
            for word, emj in emoji_dict.items():
                if emj == single_emj:
                    convert_words.append(word)
                    found = True
                    break
            
        if not found:
            print(f"'{user_input}' not found in the emoji dictionary/library")
            convert_words.append(user_input)
            
#print output
result = " ".join(convert_words)
print(f'Result: {result}')

#try again or exit
play_again = input("Do you want to try again? (yes/no): ").lower()
if play_again not in ["yes", "y"]:
    print("Thanks for using the emoji converter! Goodbye!")
    running = False
