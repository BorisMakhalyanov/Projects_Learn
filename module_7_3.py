class WordsFinder:

    change_signs = [',', '.', '=', '!', '?', ';', ':', ' - ']
    def __init__(self, *file_names):
        self.file_names = file_names

    def zamena(self, line):
        new_line = line.replace(WordsFinder.change_signs[0], '')
        for s in WordsFinder.change_signs[1:]:
            new_line = new_line.replace(s, '')
        return new_line

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                all_words[file_name] = []
                for line in file:
                    line = line.lower()
                    line = self.zamena(line)
                    for word in line.split():
                        all_words[file_name].append(word)
        return all_words

    def find(self, word):
        dictionary = {}
        for file_name, words in self.get_all_words().items():
            for pos, w in enumerate(words):
                if word.lower() == w.lower():
                    dictionary[file_name] = pos + 1
                    break
        return dictionary

    def count(self, word):
        dictionary = {}
        for file_name, words in self.get_all_words().items():
            counter = 0
            for w in words:
                if word.lower() == w.lower():
                    counter += 1
            dictionary[file_name] = counter
        return dictionary

def main():

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего

if __name__ == '__main__':
    main()
