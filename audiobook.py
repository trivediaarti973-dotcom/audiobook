from gtts import gTTS

# Read the book text
with open("book.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Convert text to speech (change "en" to "hi" for Hindi, "ko" for Korean)
tts = gTTS(text=text, lang="en", slow=False)

# Save as MP3
tts.save("audiobook.mp3")
print("Audiobook created!")