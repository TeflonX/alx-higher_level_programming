#include <Python.h>
/**
 * print_python_bytes - prints some python information
 * @p: pointer
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("[.] Size of the Python Bytes = %ld\n", size);
	printf("[.] First %ld bytes: ", size > 10 ? 10 : size);

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
		if (i + 1 < size && i + 1 < 10)
			printf(" ");
	}

	printf("\n");
}
