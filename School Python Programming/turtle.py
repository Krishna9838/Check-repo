import gtts
text=input("Enter text: ")
sound=gtts.gTTS(text, lang="eng")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")

