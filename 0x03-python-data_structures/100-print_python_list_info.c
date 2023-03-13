#include "lists.h"
/**
 * print_python_list_info - function that prints some basic info about
 * Python lists
 * @p: a pointer of type, PyObject
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	long int i, size;

	PyObject *list;

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %lu\n", size);
	for (i = 0; i < size; i++)
	{
		list = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(list)->tp_name);
	}
}
