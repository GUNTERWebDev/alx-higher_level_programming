#include "lists.h"
#include <stdlib.h>

/**
 * add_head - ad a node to the head of a linkd list
 * @head: pointer to head node
 * @node: node
 *
 * Return: return pointer to node
 */
listint_t *add_head(listint_t **head, listint_t *node)
{
	node->next = *head;
	*head = node;
	return (node);
}
/**
 * insert_node - inserts node in linked list in order
 * @head: head node
 * @number: number
 * Description: insert a new node in order
 *
 * Return: new node's adress | NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (!(*head) || (*head)->n > number)
		return (add_head(head, new_node));

	ptr = *head;
	while (ptr && ptr->next)
	{
		if (ptr->next->n > number)
			break;
		ptr = ptr->next;
	}
	new_node->next = ptr->next;
	ptr->next = new_node;
	return (new_node);
}
