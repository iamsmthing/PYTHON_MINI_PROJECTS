from googlesearch import search
query = input("What you want to search:")
 
for j in search(query, num=20, stop=10):
    print(j)