#include <unordered_set>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};



class Solution 
{
public:
    bool hasCycle(ListNode *head) 
    {
        unordered_set<ListNode*> appeared;
        
        ListNode* current = head;
        
        while (current != NULL)
        {
            if (appeared.find(current) != appeared.end())
            {
                return true;
            }
            appeared.insert(current);
            current = current->next;
        }
        return false;
    }
};