#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* result = (struct ListNode*) malloc(sizeof(struct ListNode));
    if (result == NULL) {
        return NULL;
    }

    result->val = 0; // The value of the dummy head itself doesn't matter
    result->next = NULL;

    struct ListNode* current = result; // 'current' will traverse and build the new list
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry != 0) {
        int val1 = l1 ? l1->val : 0; 
        int val2 = l2 ? l2->val : 0; 
        
        int total = val1 + val2 + carry;
        carry = total / 10; 

        // Create a new node for the current digit of the sum
        struct ListNode* newNode = (struct ListNode*) malloc(sizeof(struct ListNode));
        if (newNode == NULL) {
            return NULL; 
        }
        
        newNode->val = total % 10; // The digit for the current position
        newNode->next = NULL;

        current->next = newNode; // Link the new node to the end of the current list
        current = current->next; // Move 'current' to the newly added node

        // Move l1 and l2 pointers forward if they are not NULL
        if (l1) {
            l1 = l1->next;
        }
        if (l2) {
            l2 = l2->next;
        }
    }

    return result->next;
}

int main() {
    struct ListNode* l1 = (struct ListNode*) malloc(3 * sizeof(struct ListNode));
    l1[0].val = 2; l1[0].next = &l1[1];
    l1[1].val = 4; l1[1].next = &l1[2];
    l1[2].val = 3; l1[2].next = NULL;

    struct ListNode* l2 = (struct ListNode*) malloc(3 * sizeof(struct ListNode));
    l2[0].val = 5; l2[0].next = &l2[1];
    l2[1].val = 6; l2[1].next = &l2[2];
    l2[2].val = 4; l2[2].next = NULL;

    struct ListNode* result = addTwoNumbers(l1, l2);

    struct ListNode* current = result;
    while (current != NULL) {
        printf("%d -> ", current->val);
        current = current->next;
    }
    printf("NULL\n");
    // Free allocated memory
    free(l1);
    free(l2);
    free(result);

    return 0;
}