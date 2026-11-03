text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
text_2 = ""
for i in range(len(text)):
    if text[i] == " " and (text[i-1] != "," and text[i-1] != "."):
        text_2 += "ing "
    elif text[i] == "," or text[i] == ".":
        text_2 += "ing" + text[i]
    else:
        text_2 += text[i]
print(text_2 + "ing")
