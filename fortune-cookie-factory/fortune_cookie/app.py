import random


def open_cookie():
    text = call_text()
    print("🎉 Your fortune cookie tells 🎉")
    print(f"🍪 {text} 🍪 \n")


def call_text() -> str:
    str_list = [
        "Nothing astonishes men so much as common sense and plain dealing.", 
        "If you have something good in your life, don't let it go!", 
        "People are naturally attracted to you.", 
        "A stranger, is a friend you have not spoken to yet.",
        "A short stranger will soon enter your life with blessings to share.",
        "Now is the time to try something new.",
        "Joys are often the shadows, cast by sorrows.",
        "When fear hurts you, conquer it and defeat it!",
        "If winter comes, can spring be far behind?",
        "You are very talented in many ways.",
        "Meeting adversity well is the source of your strength.",
        "There is no greater pleasure than seeing your loved ones prosper.",
        "A very attractive person has a message for you.",
        "You are very talented in many ways.",
        "Your shoes will make you happy today.",
    ]
    
    return random.choice(str_list)
