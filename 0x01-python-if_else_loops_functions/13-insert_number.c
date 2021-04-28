#include "lists.h"

/**
 * insert_node - Is a function in C that inserts a number into a sorted singly
 * linked list.
 * @head: a pointer to the direction of the head of the linked list
 * @number: The number to add
 *Return: the new node or the head of the list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *current = *head;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = NULL;
		*head = new_node;
		return (*head);
	}

	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}

		temp->next = new_node;
		new_node->next = current;
	}

	return (new_node);
}
