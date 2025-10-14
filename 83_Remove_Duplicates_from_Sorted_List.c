#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (!head) return NULL;

    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode* curr = head;

    while (curr && curr->next) {
        if (curr->val == curr->next->val) {
            curr->next = curr->next->next;
        } 
        else{
            curr = curr->next;
        }
    }

    struct ListNode* newHead = dummy->next;
    free(dummy);
    return newHead;

}

int main() {
    

    return 0;
}