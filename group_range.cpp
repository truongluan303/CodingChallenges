/**
 * Given an array of integer, return the minimum number of possible groups so that
 * the difference between the largest and smallest values are less than or equal to
 * number k.
 *
 * Example: arr = [2, 3, 5, 1, 8, 9, 2], k = 3
 * The minimum amount of groups are: (1, 2, 2, 3), (5, 8), (9)
 * Hence, the result is 3
 */

#include <iostream>
#include <vector>
#include <cassert>
#include <bits/stdc++.h>


using namespace std;


template <typename T>
void merge_sort(vector<T>& arr, int begin, int end)
{
    if (begin < end)
    {
        int mid = (begin + end) / 2;

        merge_sort(arr, begin, mid);
        merge_sort(arr, mid + 1, end);

        int l = begin;
        int r = mid + 1;
        int i = 0;

        int left_lim = mid;
        int right_lim = end;

        T temp[end - begin + 1];

        while (l <= left_lim and r <= right_lim)
        {
            if (arr[l] <= arr[r])   temp[i++] = arr[l++];
            else                    temp[i++] = arr[r++];
        }
        while (l <= left_lim)       temp[i++] = arr[l++];
        while (r <= right_lim)      temp[i++] = arr[r++];

        int m = begin, n = 0;

        while (m < right_lim + 1)   arr[m++] = temp[n++];
    }
}

template <typename T>
void merge_sort(vector<T>& arr)
{
    merge_sort(arr, 0, arr.size() - 1);
}


size_t minimum_group(vector<int> arr, int k)
{
    merge_sort(arr);

    size_t count = 1;
    size_t begin = 0;

    for (size_t i = 0; i < arr.size(); i++)
    {
        if (arr[i] - arr[begin] > k)
        {
            begin = i;
            count++;
        }
    }
    return count;
}


int main()
{
    vector<int> arr { 2, 3, 5, 1, 8, 9, 2 };
    int k = 3;

    assert(minimum_group(arr, k) == 3);

    cout << "Passed" << endl;
    return 0;
}
