def read_by_line(file_name):
    new_str = ''
    fp = open(file_name, 'r')
    handle = fp.readlines()
    fp.close()
    for line in handle:
        new_str += line
    return new_str


def omit_vowels(line):
    vowel_count = 0
    line = line.lower
    for i in line.:
        if i == 'a' or i == 'e' or i == 'i' or i == 'u'or i == 'o':
            vowel_count += 1
            i = ''
    return line


without_vowels = omit_vowels(read_by_line('C://Users\Dilan\Desktop\Strive_AI_Projects\AI_Spring_2021\Modules\M-01-Programming Foundations\D-05-Python(GitGood)//text-files//blakepoems.txt'))
print(without_vowels)

# str_txt = ''
# new_file_handle = open('blkpms.txt', "a+")
# for ele in read_by_line('C://Users\Dilan\Desktop\Strive_AI_Projects\AI_Spring_2021\Modules\M-01-Programming Foundations\D-05-Python(GitGood)//text-files//blakepoems.txt'):
#     str_txt = omit_vowels(ele)
#
# new_file_handle.write(str_txt)