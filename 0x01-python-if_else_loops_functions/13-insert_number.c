#include "lists.h"

/**
 * insert_node - function that inserts a number
 * into a sorted singly linked list.
 *
 * @head: the head of the linked list
 * @number: the number to insert in the list
 *
 * Return: the address of the new node
 * or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (current->next)
	{
		if (current->next->n > number)
			break;
		current = current->next;
	}

	new->next = current->next;
	current->next = new;

	return (new);
}
