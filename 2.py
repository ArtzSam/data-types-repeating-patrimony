def a(text):
    texts = text.split()
    correct = []

    for i, tt in enumerate(texts):
        if i == 0 or texts[i - 1][-1] in ".!?":
            correct.append(tt.capitalize())
        else:
            correct.append(tt)

    return " ".join(correct)


text = "на этом заканчиваю свое сочинение. поставьте пятерку, Мария Ивановна! я очень старалась!"
restored_text = a(text)
print(restored_text)