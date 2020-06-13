from imdb import IMDb

ia = IMDb()
search = ia.get_top250_movies()

n = input('How much films you want? ')

for i in range(int(n)):
    print(search[i])
