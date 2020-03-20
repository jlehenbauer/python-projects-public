def solution(A):
    total = sum(A)
    Aavg = total/len(A)
    Akeep = len(A)
    for low in range(len(A)-2):
        avg = sum(A[low + 1:])/(len(A) - low - 1)
        keep = low + 1
        if A[low] >= avg:
            avg = sum(A[low + 1:])/(len(A) - low - 1)
            keep = low + 1
            #print("Found low: " + str(A[low + 1:]))
            #print("Divided by: " + str(len(A) - low - 1))
            #print("To get new avg: " + str(avg))
            #print("Starts at position: " + str(keep))
        if avg < Aavg:
            Akeep = keep
            Aavg = avg
        for high in range(low + 3, len(A))[::-1]:
            if A[high] > avg:
                avg = sum(A[low + 1:high])/(high - low -1)
                keep = low + 1
                #print("Found low: " + str(A[low + 1:high]))
                #print("Divided by: " + str(high - low - 1))
                #print("To get new avg: " + str(avg))
                #print("Starts at position: " + str(keep))
        #print("current avg: " + str(avg))
        #print("current low position: " + str(keep))
        #print("current Aavg: " + str(Aavg))
        #print("current Alow position: " + str(Akeep))
        if avg < Aavg:
            Akeep = keep
            Aavg = avg
    return Akeep