/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, greater<pair<int, ListNode*>>> pq;
        for(auto head: lists){
            if(head!=NULL){
                pq.push({head->val, head});
            }
        }
        ListNode *head = !pq.empty() ? pq.top().second : NULL, *prev = NULL;
        while(!pq.empty()){
            auto node = pq.top().second;
            pq.pop();
            if(prev!=NULL){
                prev->next = node;
            }
            prev = node;
            if(node->next!=NULL){
                pq.push({node->next->val, node->next});
            }
        }
        return head;
    }
};
