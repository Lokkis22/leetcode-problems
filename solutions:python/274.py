def hIndex(citations):
    citations.sort()
    h = 0
    i = 0
    while i < len(citations):
        if citations[i] >= h + 1 and len(citations[i:len(citations)]) >= h + 1:
            h += 1
        else:
            i += 1
        
    return h