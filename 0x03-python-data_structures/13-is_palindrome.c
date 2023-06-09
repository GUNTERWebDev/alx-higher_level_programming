#include "lists.h"

/**
 * is_palindrome - function that check if a singly linked list is a palindrome
 * @head: pointer to head node
 * Return: 0 and 1 success and failure
 */
int is_palindrome(listint_t **head)
{
	const listint_t *curr;
	int len, a, b, tmp[9999];

	if (*head == NULL)
		return (1);
	curr = *head;
	len = 0;
	while (curr != NULL)
	{
		curr = curr->next;
		len++;
	}
	if (len == 1)
		return (1);
	curr = *head;
	a = 0;
	while (curr != NULL)
	{
		tmp[a] = curr->n;
		a++;
		curr = curr->next;
	}
	b = 0;
	a--;
	len--;
	while (a >= (len / 2))
	{
		if (tmp[a] != tmp[b])
			return (0);
		a--;
		b++;
	}
	return (1);
}
