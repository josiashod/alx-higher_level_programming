#include "lists.h"
#include <stdio.h>

/**
 * reverse_list - Reverse a simply linked list
 * @head: Adress of the list to reverse
 *
 * Return: the pointer to the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev, *next;

	if (!head || !(*head))
		return (NULL);

	if (!(*head)->next)
		return (*head);

	prev = NULL;
	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Check if a singly linked list is a palindrome.
 * @head: Adress to the list to check
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	listint_t *last_node = *head, *prev = NULL;

	if (!head || !(*head))
		return (1);
	if (!(*head)->next)
		return (1);

	/* going to the end of the list */
	while (last_node->next)
		last_node = last_node->next;

	while (curr)
	{
		/* if previous element is not null */
		if (prev)
		{
			/* going to the element before the previous checked element */
			while ((last_node->next != prev) && last_node->next)
				last_node = last_node->next;

			/* stop if the last element is the same as the current element */
			if (last_node == curr)
				break;
		}
		if (last_node->n == curr->n)
		{
			/* check if the next element is not the last checked element */
			if (curr->next == last_node)
				break;

			prev = last_node;
			curr = curr->next;
			last_node = curr;
		}
		else
			return (0);
	}
	return (1);
}
