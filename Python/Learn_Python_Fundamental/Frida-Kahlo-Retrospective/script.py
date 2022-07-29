paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Potrait With Monkeys']
dates = [1939, 1933, 1946, 1940]

paintings = list(zip(paintings, dates))
print(paintings)

paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print(paintings)

paintings_length = len(paintings)
print(paintings_length)

audio_tour_number = range(1, 8)
print(list(audio_tour_number))

master_list = list(zip(audio_tour_number, paintings))
print(master_list)
