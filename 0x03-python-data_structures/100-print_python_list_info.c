#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - A C function that prints some basic info about
 * Python lists.
 * @p: a pointer
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i;
	int size = (int)PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
