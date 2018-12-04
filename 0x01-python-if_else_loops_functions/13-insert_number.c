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
	listint_t *prev, *new_node;

	if (!head)
		return (NULL);

	new_node = create_node(number);

	if (!*head)
	{
		*head = new_node;
		return (new_node);
	}
	prev = *head;
	if (number <= (*head)->n)
	{
		new_node->next = prev;
		*head = new_node;
		return (new_node);
	}
	while (prev->next)
	{
		if (number <= (prev->next)->n)
		{
			new_node->next = prev->next;
			prev->next = new_node;
			return (new_node);
		}
		prev = prev->next;
	}
	prev->next = new_node;
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
		exit(0);

	new_node->n = number;
	new_node->next = NULL;

	return (new_node);
}
