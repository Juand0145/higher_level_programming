#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - is a function in C that checks if a
 * singly linked list has a cycle in it.
 * @list: the start of the linked list.
 * Return: 0 if is not a cycle and 1 if it is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
