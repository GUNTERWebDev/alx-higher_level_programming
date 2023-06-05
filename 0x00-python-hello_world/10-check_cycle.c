#include "lists.h"

/**
 * check_cycle - Linked list cycle
 * @list: list's head node
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	if (!list)
		return (0);
	s = list;
	f = list->next;
	while (f && f->next)
	{
		if (f == s)
			return (1);
		s = s->next;
		f = f->next->next;
	}
	return (0);
}
