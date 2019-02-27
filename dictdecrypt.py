PlainKey = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890.,'"
EnigmaKey = "T'60US7,ORW 89HC3YJMKEIB1QVDXFP52ZN4ALG."
Cypher = "OV HEUV6TMJGV'KMVOV6T9.MVUTMVTVI,H UVH9UL"
Dictionary = {}
DeCypher = ''

for ch in EnigmaKey:
    newletter = (PlainKey[(EnigmaKey.find(ch))])
    Dictionary[ch] = newletter

for ch in Cypher:
    newletter = Dictionary[ch]
    DeCypher += newletter

print(DeCypher)

