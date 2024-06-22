#include <iostream>
#include <vector>

class Solution {
 public:
  void sortColors(std::vector<int>& nums) {
    int zero = -1;
    int one = -1;
    int two = -1;

    for (const int num : nums)
      if (num == 0) {
        nums[++two] = 2;
        nums[++one] = 1;
        nums[++zero] = 0;
      } else if (num == 1) {
        nums[++two] = 2;
        nums[++one] = 1;
      } else {
        nums[++two] = 2;
      }
  }
};

int main() {
    std::vector<int> colors = {1, 1, 0, 2, 0, 2};
    Solution solution;
    solution.sortColors(colors);

    for (int color : colors) {
        std::cout << color << " ";
    }
    return 0;
}
