#include "lists.h"
/**
 * check_cycle - check_cycle
 * @list: list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);
	fast = list->next;
	slow = list;

	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
