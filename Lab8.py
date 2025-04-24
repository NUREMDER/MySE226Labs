def main():
    class ArchiveItem:
        def __init__(self, uid, title, year):
            self.uid = uid
            self.title = title
            self.year = year

        def __str__(self):
            return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"

        def __eq__(self, other):
            return self.uid == other.uid

        def is_recent(self, n):
            return 2025 - self.year <= n

    class Book(ArchiveItem):
        def __init__(self, uid, title, year, author, pages):
            super().__init__(uid, title, year)
            self.author = author
            self.pages = pages

        def __str__(self):
            return f"Book -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Author: {self.author}, Pages: {self.pages}"

    class Article(ArchiveItem):
        def __init__(self, uid, title, year, journal, doi):
            super().__init__(uid, title, year)
            self.journal = journal
            self.doi = doi

        def __str__(self):
            return f"Article -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Journal: {self.journal}, DOI: {self.doi}"

    class Podcast(ArchiveItem):
        def __init__(self, uid, title, year, host, duration):
            super().__init__(uid, title, year)
            self.host = host
            self.duration = duration

        def __str__(self):
            return f"Podcast -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Host: {self.host}, Duration: {self.duration} mins"

    def save_to_file(items, filename):
        with open(filename, 'w') as file:
            for item in items:
                if isinstance(item, Book):
                    file.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
                elif isinstance(item, Article):
                    file.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
                elif isinstance(item, Podcast):
                    file.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")

    def load_from_file(filename):
        items = []
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                item_type = parts[0]
                if item_type == 'Book':
                    items.append(Book(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
                elif item_type == 'Article':
                    items.append(Article(parts[1], parts[2], int(parts[3]), parts[4], parts[5]))
                elif item_type == 'Podcast':
                    items.append(Podcast(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
        return items

    book1 = Book("B001", "Deep Learning", 2018, "Ian Goodfellow", 775)
    book2 = Book("B002", "Machine Learning", 2020, "Tom Mitchell", 600)
    article1 = Article("A101", "Quantum Computing", 2022, "Nature", "10.1234/qc567")
    article2 = Article("A102", "AI in Healthcare", 2021, "IEEE", "10.5678/ai234")
    podcast1 = Podcast("P301", "TechTalk AI", 2023, "Jane Doe", 45)
    podcast2 = Podcast("P302", "Science Daily", 2020, "John Smith", 60)

    items = [book1, book2, article1, article2, podcast1, podcast2]
    save_to_file(items, "archive.txt")
    loaded_items = load_from_file("archive.txt")

    for item in loaded_items:
        print(item)

    print("\nRecent Items:")
    for item in loaded_items:
        if item.is_recent(5):
            print(item)

    print("\nArticles with DOI starting '10.1234':")
    for item in loaded_items:
        if isinstance(item, Article) and item.doi.startswith("10.1234"):
            print(item)

if __name__ == "__main__":
    main()



