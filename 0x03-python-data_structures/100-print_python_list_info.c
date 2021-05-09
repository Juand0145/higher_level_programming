#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
* print_python_list_info - Print python list info
* @p: A pointer to PyObject, that is in PyListObject
*/

void print_python_list_info(PyObject *p)
{
    int element;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (element = 0; element < Py_SIZE(p); element++)
	{
	       printf("Element %d: ", element);
	       printf("%s\n", Py_TYPE(PyList_GetItem(p, element))->tp_name);
	}
}