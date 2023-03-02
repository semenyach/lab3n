def n31and32()
    words = []
while (new_word := str(input( ))) != "stop":
    words.append(new_word)
print(" ".join(words))
n31and32()
def n33()
    word = input("Введите слово: ")
for i in range(len(word)):
    if word[i] == "ф" or word[i] == "Ф":
        print("Ого! Это редкое слово!")
        break
    else:
        print("Эх, это не очень редкое слово...")
        break
n33()