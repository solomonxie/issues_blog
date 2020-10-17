# `Queue` (Data structure)

[Refer to wiki: Queue (abstract data type)](https://www.wikiwand.com/en/Queue_(abstract_data_type))

![image](https://user-images.githubusercontent.com/14041622/48720789-6413d300-ec5b-11e8-9ea3-b981924c4067.png)


## ADT DEFINITION

> "There are several efficient implementations of FIFO queues. An efficient implementation is one that can perform the operations—enqueuing and dequeuing—in O(1) time."

Linked list implementation of Queue:
```py
ADT: <QUEUE> (linked list)

DATA:
    - Node
        - value
        - next
    - Queue
        - root
        - length

OPERATIONS:

    __init__():

    enqueue(value):
        (*) add the new element to the last

    dequeue():
        (*) delete the first element
```

Array implementation of Queue:
```py
ADT: <QUEUE> (array)

DATA:
    - Queue
        - elements []
        - head
        - tail
```


## IMPLEMENTATION


## ANALYSIS

![image](https://user-images.githubusercontent.com/14041622/48720809-7726a300-ec5b-11e8-9046-f16b3adcf420.png)

