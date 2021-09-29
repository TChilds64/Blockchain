#Usable max index of hash
index= 45

#Creates new array of length of hash with all values as 0
#Used in dictionary for count
def newChar(dict, char):
    count = [0] * index
    dict[char]= count


#Opens txt files and creates dictionary of chars.
#Keys for each char is an array that stores the count of the number
#of instances of that char at that index over all hashes in file

#Returns dictionary and creates file for output

#params file1 to be read; file2 to be wrote to

def createDict(file1, file2):
    f= open(file1, 'r')
    dict = {}
    while(True):
        hash = f.readline()
        #check if line of file
        if not hash:
            break

    #Parses hashes
        for i in range(index):
            char = hash[i]
            if char not in dict:
                newChar(dict, char)
            dict[char][i] += 1
    
    f.close()
    
    #Creates file
    f2 = open(file2, 'w')
    keys = dict.items()
    for key in keys:
        f2.write(str(key))

    f2.close()
    return dict





#determines most common index  for each character in dictionary
def indexMax(dict):
    keys = dict.keys()
    for key in keys:
        max = 0
        counts = dict.get(key)
        for count in counts:
            if (count > max):
                max = count
        maxIndex = counts.index(max)
        print(key, max, maxIndex)


#determines least common index for each character in dictionary
def indexMin(dict):
    keys = dict.keys()
    for key in keys:
        min = index + 1
        counts = dict.get(key)
        for count in counts:
            if (count < min):
                min = count
        minIndex = counts.index(min)
        print(key, min, minIndex)


#determines average instances of char per hash
#divisor in avg is hardcoded
def avgPerHash(dict):
    keys = dict.keys()
    for key in keys:
        sum = 0
        counts = dict.get(key)
        for count in counts:
            sum = sum + count
        avg = sum/6
        
        print(key, sum, avg)
   

#Returns full hash with the most common characters per at each index
def frequentHash(dict):
    keys = dict.keys()
    hash = [""] * index
    freq = [0] * index
    for key in keys:
        counts = dict.get(key)
        for i in range(index):
            if (freq[i] < counts[i]):
                freq[i]= counts[i]
                hash[i] = key
    final = ""
    for s in hash:
        final += s
    print(final)
    print(freq)
    return final


def compareHash(filename, hash):
    f = open(filename, 'r')
    
    fileline = 0
    newList = []
    while(True):
        line = f.readline()
        #check if line of file
        if not line:
            break

        matches = 0
        for i in range(index):
            if (line[i] == hash[i]):
                matches = matches + 1
        if (matches <= 1):
            print(fileline, matches, line)
            newList.append(line)

        fileline = fileline + 1
    f.close()

    f2 = open("minRefine.txt", 'w')
    for l in newList:
        f2.write(l)
    f2.close()

#compare single hash to rest of file
def hashCompareFile(hash, filename):    
    f = open(filename, 'r')
    
    fileline = 0
    while(True):
        line = f.readline()
        #check if line of file
        if not line:
            break
        match= 0
        for i in range(index):
            if (hash[i] == line[i]):
                match += 1
        
        if (match > 7):
            print(fileline, match, line)
        fileline += 1
    
    f.close()
     






