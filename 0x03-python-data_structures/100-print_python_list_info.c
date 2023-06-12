#include <Python.h>

/**
 * print_python_list_info - function takes a Python list object (PyObject*)
 * as input and prints information about the list.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int len;
	int alloc;
	int i;
	PyObject *obj;

	len = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < len; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
