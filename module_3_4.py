def single_root_words(root_word, *other_words):
    same_words = []
    for index in range(other_words.__len__()):
        if root_word.lower() in other_words[index].lower():
                same_words.append(other_words[index])
    print(f'Корневое слово: {root_word}')
    print(f'Изначальный список: {other_words}')
    print(f'Корневой список: {same_words}')

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Able','Disablement', 'Able', 'Mable', 'Disable', 'Bagel')