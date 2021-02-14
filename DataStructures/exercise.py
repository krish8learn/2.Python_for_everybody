arr = []
file = open("nyc_weather.csv")
for line in file:
    token = line.split(',')
    try:
        arr.append(int(token[1]))
    except:
        print("ignoring")

# average:
print("the average in 1st week:",(sum(arr[0:7])/7))
print("max temp:",max(arr))
print("max temp in first 10 days:",max(arr[0:10]))

map = {}
file = open("nyc_weather.csv")
for line in file:
    token = line.split(',')
    day= token[0]
    temp = token[1]
    try:
        map[day] = int(temp)
    except:
        print("invalid row")
print(map)
print("temp on jan 9:",map['Jan 9'])
print("temp on jan 4:",map['Jan 4'])


file = open("poem.txt")
word = {}
for line in file:
    tokens = line.split(" ")
    for token in tokens:
        token = token.replace("\n"," ")
        if token in word:
            word[token]+=1
        else:
            word[token]=1
print(word)
