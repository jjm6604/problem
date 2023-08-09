N = int(input())
books = []
for _ in range(N):
    books.append(input())

book_dict = {}

for book in books:
    book_dict[book] = book_dict.get(book, 0) + 1
book_lst = list(book_dict.keys())
book_lst.sort()

MAX = 0
for book in book_lst:
    if MAX < book_dict[book]:
        MAX = book_dict[book]
        result = book

print(result)