class Solution {
public:
    /**
     * @param A: an integer array
     * @return: nothing
     */
    void sortIntegers2(vector<int> &A) {
        // write your code here
        quicksort(A, 0, A.size() - 1 );
    }
    



private:
   
   void quicksort(vector<int> &A , int start, int end) {
       if (start >= end) {
           return;
       }
       
       int l = start;
       int r = end;
       
       int pivot = A[(l + r) / 2] ;
       while (l <= r) {
           while (l <= r && A[l] < pivot) {
               l ++ ;
           }
           
           while (l <= r && A[r] > pivot){
               r -- ;
           }
           
           if( l <= r) {
               int temp = A[l];
               A[l] = A[r];
               A[r] = temp;
               l ++;
               r --;
           }
       
           
       }
     quicksort(A, start, r);
     quicksort(A, l, end);
       
   }

};