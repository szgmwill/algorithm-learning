class QuickSort(object):
    def __init__(self):
        super().__init__()
        print(f'==================Init =============')

    def sort(self, list: []):

        if not list or len(list) == 0:
            return list
        
        # select a pivot
        pivot = list[len(list) / 2]

        pass


    def partition(self, low: int, high: int, list: []) -> int:
        
        pivotIndex = (low + high) / 2
        pivotValue = list[pivotIndex]

        while(high >= low):
            if list[high] >= pivotValue:
                high+=1
            if list[high] < pivotValue:
                while (low <= high):




        # when left and right meet together, return 
        return 0
