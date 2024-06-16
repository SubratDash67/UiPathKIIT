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
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *newHead = new ListNode(-1);
        newHead->next = head;
        ListNode *currentStartBlock = head, *prevBlock = newHead, *nextBlock = NULL; // 1st node in a block of size k
        while(currentStartBlock!=NULL){
            ListNode *temp = currentStartBlock;
            int i = 1; 
            while(i<=k && temp!=NULL){
                i++;
                temp = temp->next;
            }
            if(i==k+1){
                nextBlock = temp;
                ListNode *prev = nextBlock, *curr = currentStartBlock, *next;
                while(curr!=nextBlock){
                    next = curr->next;
                    curr->next = prev;
                    prev = curr;
                    curr = next;
                }
                if(prevBlock!=NULL){
                    prevBlock->next = prev;
                }
                prevBlock = currentStartBlock;
                currentStartBlock = nextBlock;
            }else{
                break;
            }
        }
        return newHead->next;
    }
};
