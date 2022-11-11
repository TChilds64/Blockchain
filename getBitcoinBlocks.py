import blockchain as b
import time

start= time.time() 
f = open("b.txt", 'w')
new = b.blockexplorer.get_latest_block()
tempHash= new.hash
hash= tempHash[18:]
block = b.blockexplorer.get_block(tempHash)

check = 0
for i in range(500):
    f.write(hash+'\n')

    prev= block.previous_block
    block = b.blockexplorer.get_block(prev)
    tempHash = block.hash
    hash= tempHash[19:]
    check = i

f.close()
end = time.time()
final = end - start
print("success " + str(final) + str(check))




