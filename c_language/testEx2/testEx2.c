#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Python.h"

int fac(int n)
{
	if (n < 2) return(1); /* 0! == 1! == 1 */
	return (n)*fac(n - 1); /* n! == n*(n-1)! */
}

char *reverse(char *s)
{
	register char t, /* tmp */
		*p = s, /* fwd */
		*q = (s + (strlen(s) - 1)); /* bwd */

	while (p < q) /* if p < q */
	{ /* swap & mv ptrs */
		t = *p;
		*p++ = *q;
		*q-- = t;
	}
	return s;
}

int test()
{
	char s[BUFSIZ];
	printf("4! == %d\n", fac(4));
	printf("8! == %d\n", fac(8));
	printf("12! == %d\n", fac(12));
	strcpy_s(s, strlen("abcdef") + 1, "abcdef");
	printf("reversing 'abcdef', we get '%s'\n", reverse(s));
	strcpy_s(s, strlen("madam") + 1, "madam");
	printf("reversing 'madam', we get '%s'\n", reverse(s));
	return 0;
}

static PyObject *
Extest_fac(PyObject *self, PyObject *args)
{
	int num;
	if (!PyArg_ParseTuple(args, "i", &num))
		return NULL;
	return (PyObject*)Py_BuildValue("i", fac(num));
}

static PyObject *
Extest_doppel(PyObject *self, PyObject *args)
{
	char *orig_str;
	char *dupe_str;
	PyObject* retval;

	if (!PyArg_ParseTuple(args, "s", &orig_str))
		return NULL;
	retval = (PyObject*)Py_BuildValue("ss", orig_str, dupe_str = reverse(_strdup(orig_str)));
	free(dupe_str);
	return retval;
}

static PyObject *
Extest_test(PyObject *self, PyObject *args)
{
	test();
	return (PyObject*)Py_BuildValue("");
}

static PyMethodDef
ExtestMethods[] =
{
{ "fac", Extest_fac, METH_VARARGS },
{ "doppel", Extest_doppel, METH_VARARGS },
{ "test", Extest_test, METH_VARARGS },
{ NULL, NULL },
};

static struct PyModuleDef Extestmodule = {//必须在模块定义结构中引用方法表：
	PyModuleDef_HEAD_INIT,
	"extest",   /* name of module */
	NULL, /* 模块文档，这里没有 */
	-1,       /* size of per-interpreter state of the module,
			  or -1 if the module keeps state in global variables. */
	ExtestMethods
};

PyMODINIT_FUNC//模块初始化，传入前面的模块定义结构，返回python object，也就是导出函数
PyInit_extest(void)
{
	return PyModule_Create(&Extestmodule);
}

