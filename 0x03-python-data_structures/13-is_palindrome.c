#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
int is_palindrome(listint_t **head)
{
	listint_t *p, *arr, *assign;

	int i, j, count, loop, ret_val;

	p = assign = *head;
	count = 0;
	while (p != NULL)
	{
		count++;
		p = p->next;
	}
	printf("count = %d\n", count);
	arr = malloc(sizeof(listint_t) * count);
	for (i = 0; i < count; i++)
	{
		assign->n = arr[i].n;
		assign = assign->next;
		printf("assign->n = %d, arr[i].n = %d\n",
			assign->n, arr[i].n);
	}
	
	ret_val = 0;
	loop = count / 2;
	for (j = 0; j < loop; j++)
	{
/*		printf("arr[i].n = %d, arr[count - 1 - %d].n = %d\n",
			arr[i].n, arr[count - 1 - i].n);
*/		if (arr[i].n != arr[count - 1 - i].n)
			break;
		ret_val++;
	}
	printf("loop = %d\nret_val = %d\n", loop, ret_val);
	if (ret_val == loop)
		return (1);
	else
		return (0);
}
