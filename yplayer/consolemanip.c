#include <Python.h>

/*
* function to clear current cursor line
*/
static PyObject* clear_line(PyObject* self)
{
	const char* CLEAR_LINE = "\033[K";

	//build a python object returning a line-clearing command
	return Py_BuildValue("s", CLEAR_LINE); 
}


/*
* function to navigate up one cursor line
*/
static PyObject* up_line(PyObject* self)
{
	const char* UP_LINE = "\033[F";

	//build a python object returning a line-clearing command
	return Py_BuildValue("s", UP_LINE); 
}



static PyMethodDef clearLineMethods[] = 
{
	{"clear_line", clear_line, METH_NOARGS,  "Clears cursor's current row and performs a carriage return."},
	{"up_line", up_line, METH_NOARGS, "Moves cursor's current position up one row."},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initConsoleManip(void)
{
	(void)Py_InitModule("ConsoleManip", clearLineMethods);
}

