# 🥴
# 😜

# from unittest import result


msg = input("> ")
words = msg.split(" ")

emojis = {
    ":)":"🥴",
    "(:":"😜"
}
result = ""
for word in words:
    result += emojis.get(word, word) + " "
print(result)