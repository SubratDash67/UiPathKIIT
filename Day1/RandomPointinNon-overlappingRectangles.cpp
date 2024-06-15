class Solution
{
public:
  vector<vector<int>> rects_b;
  vector<int> points_until;

  Solution(vector<vector<int>> &rects)
  {
    for (auto &e : rects)
    {
      int before = (points_until.size() == 0) ? 0 : points_until.back();
      points_until.push_back((e[2] - e[0] + 1) * (e[3] - e[1] + 1) + before);
      rects_b = rects;
    }
  }

  vector<int> pick()
  {
    int ind = rand() % points_until.back();
    int rect = upper_bound(points_until.begin(), points_until.end(), ind) - points_until.begin();
    ind -= (rect == 0) ? 0 : points_until[rect - 1];
    int row = rects_b[rect][3] - rects_b[rect][1] + 1;
    return {ind / row + rects_b[rect][0], ind % row + rects_b[rect][1]};
  }
};
