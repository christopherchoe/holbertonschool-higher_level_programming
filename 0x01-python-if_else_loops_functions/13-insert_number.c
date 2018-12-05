#include <stdlib.h>
#include <stdio.h>
#include <time.h>
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
	listint_t *new_node;
	listint_t *current;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;

	current = *head;
	if (current)
	{
		if (current->n > number)
		{
			new_node->next = current;
			*head = new_node;
		}
		else
		{
			while (current && current->next)
			{
				if (current->next->n < number)
					current = current->next;
				else
					break;
			}
			new_node->next = current->next;
			current->next = new_node;
		}
	}
	else
	{
		*head = new_node;
		new_node->next = NULL;
	}
	return (new_node);
}
