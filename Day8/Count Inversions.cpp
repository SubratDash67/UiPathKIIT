#include <iostream>
#include <vector>

int mergeAndCount(std::vector<int>& arr, int left, int mid, int right) {
    std::vector<int> leftArr(arr.begin() + left, arr.begin() + mid + 1);
    std::vector<int> rightArr(arr.begin() + mid + 1, arr.begin() + right + 1);

    int i = 0, j = 0, k = left, swaps = 0;

    while (i < leftArr.size() && j < rightArr.size()) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k++] = leftArr[i++];
        } else {
            arr[k++] = rightArr[j++];
            swaps += (mid + 1) - (left + i);
        }
    }

    while (i < leftArr.size()) {
        arr[k++] = leftArr[i++];
    }

    while (j < rightArr.size()) {
        arr[k++] = rightArr[j++];
    }

    return swaps;
}

int mergeSortAndCount(std::vector<int>& arr, int left, int right) {
    int count = 0;
    if (left < right) {
        int mid = left + (right - left) / 2;

        count += mergeSortAndCount(arr, left, mid);
        count += mergeSortAndCount(arr, mid + 1, right);

        count += mergeAndCount(arr, left, mid, right);
    }
    return count;
}

int main() {
    std::vector<int> arr = {70, 50, 60, 10, 20, 30, 80, 15};
    int n = arr.size();
    int result = mergeSortAndCount(arr, 0, n - 1);
    std::cout << "Number of inversions are: " << result << std::endl;
    return 0;
}
