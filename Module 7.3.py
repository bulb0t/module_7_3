from itertools import count


class WordsFinder:
    def __init__(self, *file):
        self.file_names = file

    def get_all_words(self):
        all_words = {}
        for text in self.file_names:
            with open(text, encoding='utf-8') as file:
                s = ''
                for line in file:
                    for word in line:
                        str_file = word.lower().strip(',.=()!?:;-')
                        s += str_file
                list_file = s.split()
                all_words[str(text)] = list_file

        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                return {name: words.index(word.lower()) + 1}

    def count(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                return {name: words.count(word.lower())}

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


