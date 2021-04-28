import time

def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['#66ff99' if x == j or x == j+1 else 'blue' for x in range(len(data))] )
                time.sleep(timeTick)
    drawData(data, ['#66ff99' for x in range(len(data))])
    




