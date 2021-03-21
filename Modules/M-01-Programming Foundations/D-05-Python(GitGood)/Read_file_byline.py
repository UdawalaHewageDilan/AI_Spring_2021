def count_words(x):
    """Given a text return a dictionary with present
    words and frequency"""

    import re
    x = x.lower()
    words = re.sub(pattern="[^\w\s]", repl=" ", string=x).split()
    dict_count = {}
    for word in words:
        dict_count[word] = dict_count.get(word, 0) + 1
    return dict_count


def read_by_line(file_name):
    new_str =''
    fp = open(file_name, 'r')
    handle = fp.readlines()
    fp.close()
    for line in handle:
        new_str += line
    return new_str


text = read_by_line('C://Users\Dilan\Desktop\Strive_AI_Projects\AI_Spring_2021\Modules\M-01-Programming Foundations\D-05-Python(GitGood)//text-files//blakepoems.txt')
print(count_words(text))
