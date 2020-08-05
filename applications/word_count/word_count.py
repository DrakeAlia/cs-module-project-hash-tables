def word_count(s):
    # Your code here

# Case should be ignored. Output keys must be lowercase.
# Key order in the dictionary doesn't matter.
# Split the strings into words on any whitespace.
# Ignore each of the following characters:

    counts = {}

    words = s.lower().split()

    ignore = [
        ":",
        ";",
        ",",
        ".",
        "-",
        "+",
        "=",
        "/",
        "\\",
        "|",
        "[",
        "]",
        "{",
        "}",
        "(",
        ")",
        "*",
        "^" 
        "&",
        '"',
    ]

    # replacer = re.sub(ignore, "", words)
    # ignored = s.replace('"', " ")
    for w in words:
        for special in ignore:
            w = w.replace(special, " ")
        if w != "":
            if w in counts:
                counts[w] = counts[w] + 1
            else:
                counts[w] = 1
    return counts
            

if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            "This is a test of the emergency broadcast network. This is only a test."
        )
    )