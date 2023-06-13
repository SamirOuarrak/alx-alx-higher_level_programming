#include "lists.h"

/**
 * is_palindrome - chacks wether a singly linked list is a palindrome
 * @head: a pointr to a pointer to the first element of the list
 * Return: 0 if it is not palindrome, or 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head; 
	listint_t *end = *head;
	int count = 0;
	int i = 0;
	int j = 0;

	if (!*head|| !(*head)->next)
		return (1);
	while (ptr)
	{
		ptr = ptr->next;
		count++;
	}
	ptr = *head;
	for (i = 1; i <= count; i++)
	{
		for (j = i; j <= count - i; j++)
			end = end->next;
		if (ptr->n != end->n)
			return (0);
		ptr = ptr->next;
		end = ptr;
	}
	return (1);
}