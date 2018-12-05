#include <stdlib.h>
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
	listint_t *tmp, *pleasegod;

	pleasegod = malloc(sizeof(listint_t *));
	if (!pleasegod || !head)
		return (NULL);
	pleasegod->next = NULL;
	pleasegod->n = number;
	tmp = *head;
	if (!*head || (*head)->n >= number)
	{
		pleasegod->next = tmp;
		*head = pleasegod;
		return (pleasegod);
	}
	while (tmp->next)
	{
		if (number <= (tmp->next)->n)
		{
			pleasegod->next = tmp->next;
			tmp->next = pleasegod;
			return (pleasegod);
		}
		tmp = tmp->next;
	}
	if ((*head)->next == NULL || tmp->next == NULL)
	{
		tmp->next = pleasegod;
		return (pleasegod);
	}
	return (NULL);
}
