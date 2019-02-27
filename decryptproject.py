PlainKey = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890.,'"
EnigmaKey = "T'60US7,ORW 89HC3YJMKEIB1QVDXFP52ZN4ALG."
Cypher = "OV HEUV6TMJGV'KMVOV6T9.MVUTMVTVI,H UVH9UL"
DeCypher = ''

for ch in Cypher:
    oldletter = ch
    newletter = (PlainKey[(EnigmaKey.find(oldletter))])
    DeCypher += newletter

print(DeCypher)
