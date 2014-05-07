package findarray;

import java.util.*;

public class MyFindArray implements FindArray {
    // Test
    /*
    public static void main(String[] args) {
        MyFindArray mfa = new MyFindArray();
        int[] arr = new int[]{0,1,2,3,4,5};
        int[] subarr = new int[]{3,4};
        int[] subarr_2 = new int[]{3,4,6}; 
        System.out.println(mfa.findArray(arr, subarr)); // 3
        System.out.println(mfa.findArray(arr, subarr_2)); // -1
    }*/

    public int findArray(int[] array, int[] subArray) {
        List<Integer> arr_l = new ArrayList<Integer>();
        for (int i = 0; i < array.length; i++)
        {
            arr_l.add(array[i]);
        }


        List<Integer> subarr_l = new ArrayList<Integer>();
        for (int i = 0; i < subArray.length; i++)
        {
            subarr_l.add(subArray[i]);
        }

        return Collections.indexOfSubList(arr_l, subarr_l);
    }
}