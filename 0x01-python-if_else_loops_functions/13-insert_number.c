#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
  * insert_node - inserts a node in proper place of sorted list
  *
  * @head: first node of linked list
  * @number: number to add in linked list
  * Return: Address of new node or NULL if failure
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *next, *new_node;

	if (!head || !*head)
		return (NULL);

	prev = *head;
	next = *head;
	next = next->next;

	while (next && next->next)
	{
		if (number < prev->n)
			return (NULL);
		if (number == prev->n)
		{
			new_node = create_node(number);
			if (!new_node)
				return (NULL);
			prev->next = new_node;
			new_node->next = next;
			return (new_node);
		}
		prev = prev->next;
		next = next->next;
	}
	new_node = create_node(number);
	if (!new_node)
		return (NULL);

	return (new_node);
}

/**
  * create_node - creates a new node
  *
  * @number: the number to be the value for node
  * Return: the new node or NULL if failure
  */
listint_t *create_node(int number)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t *));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	return (new_node);
}
