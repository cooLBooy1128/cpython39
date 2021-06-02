#include "Python.h"//先include<Python.h>，在include别的，Python.h可能会有一些预处理定义
 
static PyObject *SpamError;
 
static PyObject *
spam_system(PyObject *self, PyObject *args)//模型封装
{
	const char *command;
	int sts;
 
	if (!PyArg_ParseTuple(args, "s", &command))//只要传进来参数，就执行system(command)
		return NULL;
	sts = system(command);
	if (sts < 0) {//排除异常，进行异常报错
		PyErr_SetString(SpamError, "System command failed");
		return NULL;
	}
	return PyLong_FromLong(sts);//执行完之后返回一个整数python object
}
 
static PyMethodDef SpamMethods[] = {//方法列表
{"system",  spam_system, METH_VARARGS,
"Execute a shell command."},
{NULL, NULL, 0, NULL}        /* Sentinel */
};
 
static struct PyModuleDef spammodule = {//必须在模块定义结构中引用方法表：
	PyModuleDef_HEAD_INIT,
	"spam",   /* name of module */
	NULL, /* 模块文档，这里没有 */
	-1,       /* size of per-interpreter state of the module,
			  or -1 if the module keeps state in global variables. */
	SpamMethods
};
 
PyMODINIT_FUNC//模块初始化，传入前面的模块定义结构，返回python object，也就是导出函数
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}
 
int main(int argc, char *argv[])
{
	wchar_t *program = Py_DecodeLocale(argv[0], NULL);
	if (program == NULL) {
		fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
		exit(1);
	}
 
	/* Add a built-in module, before Py_Initialize */
	PyImport_AppendInittab("spam", PyInit_spam);
 
	/* Pass argv[0] to the Python interpreter */
	Py_SetProgramName(program);
 
	/* Initialize the Python interpreter.  Required. */
	Py_Initialize();
 
	/* Optionally import the module; alternatively,
	import can be deferred until the embedded script
	imports it. */
	PyImport_ImportModule("spam");
 
	PyMem_RawFree(program);
	return 0;
}
