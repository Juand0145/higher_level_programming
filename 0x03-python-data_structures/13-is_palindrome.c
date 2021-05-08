#include "lists.h"

/**
*
*/
listint_t *rever_list(listint_t **head)
{
    struct listint_s *next = NULL;
    struct listint_s *prev = NULL;

    while (*head != NULL)
    {
        next = (*head)->next;
        (*head)->next = prev;
        prev = (*head);
        (*head) = next;
    }

    (*head) = prev;
    return (*head);
}

/**
*
*/
int is_palindrome(listint_t **head)
{
    int counter, i;
    listint_t *temp_1  = *head, *temp_2 = *head, *new_list, *reverse_list;

    if (*head == NULL)
        return (1);

    for (counter = 0; temp_1 != NULL; counter++)
        temp_1 = temp_1->next;

    new_list = malloc(sizeof(listint_t) * counter);

    for (i = 0; temp_2 != NULL; i++)
    {
        new_list[i].n = temp_2->n;
        new_list[i].next = &new_list[i + 1];
        temp_2 = temp_2->next;
    }

    new_list[counter - 1].next = NULL;

    reverse_list = rever_list(head);

    while (reverse_list != NULL)
    {

	    if (new_list->n == reverse_list->n)
	    {
		    new_list = new_list->next;
		    reverse_list = reverse_list->next;
	    }

	    else
		    return (0);
    }

    return (1);
}
