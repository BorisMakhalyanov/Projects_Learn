def all_variants(text):

    for length in range(1, len(text)+1):
        for i in range(len(text)):
            result = text[i]
            if length > 1:
                for j in range(len(text)):
                    if j <= i:
                        continue
                    if not text[j] in result:
                        result += text[j]
                    if len(result) == length:
                        yield result
                        result = text[i]
            else:
                yield result

def main():
    a = all_variants("1357")
    for i in a:
        print(i)

if __name__ == '__main__':
    main()
