#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stddef.h>

/**
 * print_dlistint - print the contents of a doublu linked list
 * @h: the head to the list
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *dCopy;
	size_t n = 0;

	dCopy = h;

	if (dCopy == NULL)
		return (n);

	while (dCopy != NULL)
	{
		printf("%i\n", dCopy->n);
		dCopy = dCopy->next;
		n++;
	}

	return (n);
}
