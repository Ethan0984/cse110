max = -1
maxbook = ""
with open("books_and_chapters.txt") as books:
    for line in books:
        cleanline = line.strip()
        words = cleanline.split(":")
        scripture = words[2]
        chapter = int(words[1])
        book = words[0]
        print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")
        if chapter > max:
            max = chapter
            maxbook = book
print(f"The largest amount of chapters is: {max}")
print(f"{maxbook} is the book with this many chapters.")