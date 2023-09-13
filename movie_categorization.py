
def read_ratings_data(f):
    dict1=dict()
    key_list=list()
    value_list=list()
    key_value_list=list()
    a=f.readlines()
    for line in a:
        key,value,extra=line.split("|")
        key_value_list.append([key,value])
        key_list.append(key)
        value_list.append(value)
    for i in key_list:
        dict1[i]=list()
    keys=dict1.keys()
    for i in keys:
        for j in key_value_list:
            if i==j[0]:
                dict1[i].append(j[1])
    return dict1

def read_movie_genre(f):
    a=f.readlines()
    dict2=dict()
    for line in a:
        value,extra,key=line.split("|")
        key=key.strip()
        dict2[key]=value
    return dict2

def create_genre_dict(d):
    dict3=dict()
    l=list(d.items())
    genre=list(d.values())
    for i in genre:
        dict3[i]=list()
    keys=dict3.keys()
    for i in keys:
        for j in l:
            if i==j[1]:
                dict3[i].append(j[0])
    return dict3

def calculate_average_rating(d):
    dict4=dict()
    keys=list(d.keys())
    ratings=list()
    k=list()
    for i in d.values():
        for j in i:
            k.append(float(j))
        ratings.append(round(sum(k)/len(k),2))
    dict4 = dict(zip(keys, ratings))
    return dict4

def get_popular_movies(d,n=10):
    dict5=dict()
    l=list(d.items())
    length=len(l)
    for i in range(length-1):
        for j in range(i+1,length):
            if l[i][1]<l[j][1]:
                t=l[i]
                l[i]=l[j]
                l[j]=t
    for i in range(n):
        try:
            dict5[l[i][0]]=l[i][1]
        except IndexError:
            break
    return dict5

def filter_movies(d,thres_rate=3.0):
    dict6=dict()
    l=list(d.items())
    length=len(l)
    for i in range(length):
        if l[i][1]>=thres_rate:
            dict6[l[i][0]]=l[i][1]
    return dict6

def get_popular_in_genre(genre,d1,d2,n=5):
    dict7=dict()
    list1=list(d1.items())
    list2=list(d2.items())
    list3=list()
    length1=len(list1)
    length2=len(list2)
    for i in range(length1):
        if genre==list1[i][0]:
            list3=list1[i][1]
    length3=len(list3)
    for i in range(length3):
        for j in range(length2):
            if list3[i]==list2[j][0]:
                dict7[list2[j][0]]=list2[j][1]
    dict7=get_popular_movies(dict7,n)
    print("3.3 get popular in genre movies")
    print(dict7)
    print()
    return dict7

def  get_genre_rating(genre,d1,d2):
    dict8=dict()
    list1=list(d1.items())
    list2=list(d2.items())
    list3=list()
    length1=len(list1)
    length2=len(list2)
    for i in range(length1):
        if genre==list1[i][0]:
            list3=list1[i][1]
    length3=len(list3)
    for i in range(length3):
        for j in range(length2):
            if list3[i]==list2[j][0]:
                dict8[list2[j][0]]=list2[j][1]
    tup1=dict8.values()
    try:
        avg_rating=round(sum(tup1)/len(tup1),2)
    except ZeroDivisionError:
        print("Enter valid genre name")
        avg_rating=0
    return avg_rating

def genre_popularity(d1,d2,n=5):
    dict9=dict()
    list1=list(d1.items())
    list3=list()
    length1=len(list1)
    for i in range(length1):
        list3.append(list1[i][0])
    length3=len(list3)
    for i in list3:
        dict9[i]=get_genre_rating(i,d1,d2)
    dict9=get_popular_movies(dict9,n)
    return dict9

def read_user_ratings(f):
    dict10=dict()
    key_list=list()
    value_list=list()
    key_value_list=list()
    a=f.readlines()
    for line in a:
        movie,rating,userid=line.split("|")
        userid=userid.strip()
        key_value_list.append([userid,(movie,rating)])
        key_list.append(userid)
        value_list.append((movie,rating))
    for i in key_list:
        dict10[i]=list()
    keys=dict10.keys()
    for i in keys:
        for j in key_value_list:
            if i==j[0]:
                dict10[i].append(j[1])
    return dict10

def get_user_genre(userid,d1,d2):
    list1=list(d1.items())
    list2=list(d2.items())
    list3=list()
    list4=list()
    list5=list()
    for i in range(len(list1)):
        if userid==list1[i][0]:
            list3=list1[i][1]
    for i in range(len(list3)):
        for j in range(len(list2)):
            if list3[i][0]==list2[j][0]:
                list4.append([list2[j][1],list3[i][1]])
    for i in range(len(list4)):
        genre=list4[i][0]
        ratings=list()
        for j in list4:
            if genre==j[0]:
                ratings.append(float(j[1]))
        rate=sum(ratings)/len(ratings)
        list5.append([genre,rate])
    max_rate=list5[0][1]
    for i in list5:
        if i[1]>max_rate:
            max_rate=i[1]
            genre=i[0]
    return genre

def recommend_movies(userid,d1,d2,d3):
    dict12=dict()
    list1=list(d1.items())
    list2=list(d2.items())
    list3=list(d3.items())
    list4=list()
    list5=list()
    list6=list()
    list7=list()
    genre=get_user_genre(userid,d1,d2)
    for i in range(len(list1)):
        if userid==list1[i][0]:
            list4=list1[i][1]
            break
    for j in range(len(list2)):
        if genre==list2[j][1]:
            list5.append(list2[j][0])
    for i in list5:
        for j in list3:
            if i == j[0]:
                list6.append(j)
    for i in list6:
        flag=0
        for j in list4:
            if i[0]==j[0]:
                flag=1
        if flag==0:
            list7.append(i)
    length=len(list7)
    if length>3:
        for i in range(3,length):
            list7.pop(i)
    dict12=dict(list7)
    return dict12
    
                             
        


rfile=open("movieRatingSample.txt","r")
read_ratings_dict=read_ratings_data(rfile)
print(read_ratings_dict)

gfile=open("genreMovieSample.txt","r")
read_movie_genre_dict=read_movie_genre(gfile)
print(read_movie_genre_dict)

genre_dict=create_genre_dict(read_movie_genre_dict)
print(genre_dict)

avg_rate_dict=calculate_average_rating(read_ratings_dict)
print(avg_rate_dict)

n=int(input("Enter the number of popular movies you want to see : "))
popular_movies_dict=get_popular_movies(avg_rate_dict,n)
print(popular_movies_dict)

thres_rate=float(input("Enter the minimum rating : "))
thres_movies_dict=filter_movies(avg_rate_dict,thres_rate)
print(thres_movies_dict)

genre=input("Enter the genre name for movies: ")
n=int(input("Enter the number of movies: "))
genre=genre.lower()
genre=genre.title()
popular_genre_dict=get_popular_in_genre(genre,genre_dict,avg_rate_dict,n)
print(popular_genre_dict)

genre=input("Enter the genre name for ratings: ")
genre=genre.lower()
genre=genre.title()
genre_rating= get_genre_rating(genre,genre_dict,avg_rate_dict)
print(genre_rating)

n=int(input("Enter the number of popular genres you want to see : "))
genre_popularity_dict=genre_popularity(genre_dict,avg_rate_dict,n)
print(genre_popularity_dict)

rfile.seek(0)
user_ratings_dict=read_user_ratings(rfile)
print(user_ratings_dict)

userid=input("Enter the user id for favourite genre: ")
user_genre_name=get_user_genre(userid,user_ratings_dict,read_movie_genre_dict)
print(user_genre_name)

userid=input("Enter the user id for top unrated movies: ")
recommend_movies_dict=recommend_movies(userid,user_ratings_dict,read_movie_genre_dict,avg_rate_dict)
print(recommend_movies_dict)
