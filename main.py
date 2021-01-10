import random

with open("word_rus.txt", encoding="UTF-8") as file:
    vocabulary = [row.strip() for row in file]

random.shuffle(vocabulary)

word = input("Твоё первое слово?\n").lower()
first = True
said_bot_word = ""

said_words = []

while True:
    if word not in vocabulary:
        if word in said_words:
            word = input("Слово уже было сказано! Введи правильное слово:\n").lower()
            continue

        word = input("Слова нет в словаре! Введи правильное слово:\n").lower()
        continue

    else:
        if not first:
            words_player = [k for k in vocabulary if k[0] == said_bot_word[-1]]
            index = -2
            while len(words_player) == 0:
                words_player = [k for k in vocabulary if k[0] == said_bot_word[index]]
                index -= 1

            if word not in words_player:
                word = input("Напиши слово начинающееся на последнюю букву сказанного мной слова!\n").lower()
                continue

        first = False

        words = [k for k in vocabulary if k[0] == word[-1]]
        index = -2
        while len(words) == 0:
            words = [k for k in vocabulary if k[0] == word[index]]
            index -= 1

        said_bot_word = random.choice(words)
        print(f"{said_bot_word}\n")
        vocabulary.remove(said_bot_word)
        vocabulary.remove(word)
        said_words.append(said_bot_word)
        said_words.append(word)
        word = input("\n").lower()
        continue
