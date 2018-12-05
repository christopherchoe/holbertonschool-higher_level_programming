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
	listint_t *tmp, *pleasegod;

	pleasegod = malloc(sizeof(listint_t *));
	if (!pleasegod || !head)
		return (NULL);
	pleasegod->n = number;
	tmp = *head;
	if (tmp)
	{
		if (tmp->n >= number)
		{
			pleasegod->next = tmp;
			*head = pleasegod;
		}
		else
		{
			while (tmp->next)
			{
				if (tmp->next->n < number)
					tmp = tmp->next;
				else
					break;
			}
			pleasegod->next = tmp->next;
			tmp->next = pleasegod;
		}
	}
	else
	{
		*head = pleasegod;
		pleasegod->next = NULL;
	}
	return (pleasegod);
}
