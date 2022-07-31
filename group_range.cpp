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





size_t minimum_group(vector<int> arr, int k)
{
    sort(arr.begin, arr.end);

    size_t count = 1;
    size_t begin = 0;

    for (size_t i; i < arr.size(); i++)
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
