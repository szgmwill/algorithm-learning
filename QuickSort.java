public class QuickSort {

    public int[] sort(int[] array) {
        if (array == null || array.length <= 1) {
            return array;
        }
        //sort
        quickSort(array, 0, array.length - 1);
        return array;
    }

    private void quickSort(int[] array, int left, int right) {
        if (left >= right) {
            return;
        }
        // set the pivot
        int pivot = (left + right) / 2;

        // do the process
        int index = partition(array, pivot, left, right);

        // recursion
        // left sub array
        quickSort(array, left, index - 1);
        // right sub array
        quickSort(array, index, right);
    }

    private int partition(int[] array, int pivot, int left, int right) {
        while (left <= right) {
            while (array[left] < array[pivot]) {
                left++;
            }

            while (array[right] > array[pivot]) {
                right--;
            }

            if (left <= right) {
                swap(array, left, right);
                left++;
                right--;
            }
        }
        return left;
    }

    private void swap(int[] array, int i, int j) {
        int target = array[i];
        array[i] = array[j];
        array[j] = target;
    }


    public static void main(String[] args) {
        int[] testArray = {0,2,5,4,7,11,-2,1,1,10};

        QuickSort quickSort = new QuickSort();
        quickSort.sort(testArray);

        for(int i = 0; i < testArray.length; i++) {
            System.out.println("================result: " + testArray[i]);
        }
        
    }
}