# Storing Objects in List :
class Movies(object):
    def __init__(self,title,runtime,hero):
        self.title = title
        self.runtime = runtime
        self.hero = hero
    def Printer(self):
        print(f"Title of the Movie is :{self.title}\nand Runtime is in minutes :{self.runtime}\nHero of the movie is :{self.hero}")
list_of_movies = []
while True:
    title = input("Enter the title of the movie :")
    runtime = input("Enter the runtime of the movie :")
    hero = input(" Enter the name of hero of a movie :")
    obj = Movies(title,runtime,hero)
    list_of_movies.append(obj)
    print("Movies are added into a list ")
    ans = input("Do you want to add another movie(y/n)")
    if ans!='y':
        break
print("All movies information :")
for obj in list_of_movies:
    obj.Printer()



