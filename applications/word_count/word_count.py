# Case should be ignored. Output keys must be lowercase.
# Key order in the dictionary doesn't matter.
# Split the strings into words on any whitespace.
# Ignore each of the following characters:

def word_count(s):
    # Your code here

    # count_dict = {}
    # words = ""
    # punct_ignore = '":;,.-+=/\|[]{}()*^&'
    # punct_count = 0

    # for char in s:
    #     if char in punct_ignore:
    #         punct_count +=1

    #     if char not in punct_ignore:
    #         words = words + char

    # if punct_count == 0:
    #     return count_dict

    # else:
    #     words = words.split()
    #     words = [word.lower() for word in words]

    #     for word in words:
    #         if word in count_dict:
    #             count_dict[word] +=1

    #         else:
    #             count_dict[word] = 1

    #     return count_dict


    # cache = {}

    # words_lowercased = s.lower()

    # ignored_chars = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

    # for chars in ignored_chars:

    #     words_lowercased = words_lowercased.replace(chars, "")
    # for words in words_lowercased.split():
    #     print(words)

    #     if words == "":
    #         continue
    #     if words not in cache:
    #         cache[words] = 1
    #     else:
    #         cache[words] += 1
    # return cache


    char_exclude = r'" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    words = s.lower()
    name = s.translate({ord(c): " " for c in char_exclude})
    if name == "":
        return {}
    seperate = name.lower().split()
    words = {i: seperate.count(i) for i in seperate}
    return words
 

    # cache = {}
    # s = s.lower()
    # for i in s:
    #     if i >= 'a' and i <='z':
    #         if i not in cache:
    #             cache[i] = 1
    #         else:
    #             cache[i] += 1
    # for i in cache:
    #     print(f'Letter: {i[0]}, Count: {cache[i]}')
   
            

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))