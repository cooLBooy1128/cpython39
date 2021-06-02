#include "Python.h"//��include<Python.h>����include��ģ�Python.h���ܻ���һЩԤ������
 
static PyObject *SpamError;
 
static PyObject *
spam_system(PyObject *self, PyObject *args)//ģ�ͷ�װ
{
	const char *command;
	int sts;
 
	if (!PyArg_ParseTuple(args, "s", &command))//ֻҪ��������������ִ��system(command)
		return NULL;
	sts = system(command);
	if (sts < 0) {//�ų��쳣�������쳣����
		PyErr_SetString(SpamError, "System command failed");
		return NULL;
	}
	return PyLong_FromLong(sts);//ִ����֮�󷵻�һ������python object
}
 
static PyMethodDef SpamMethods[] = {//�����б�
{"system",  spam_system, METH_VARARGS,
"Execute a shell command."},
{NULL, NULL, 0, NULL}        /* Sentinel */
};
 
static struct PyModuleDef spammodule = {//������ģ�鶨��ṹ�����÷�����
	PyModuleDef_HEAD_INIT,
	"spam",   /* name of module */
	NULL, /* ģ���ĵ�������û�� */
	-1,       /* size of per-interpreter state of the module,
			  or -1 if the module keeps state in global variables. */
	SpamMethods
};
 
PyMODINIT_FUNC//ģ���ʼ��������ǰ���ģ�鶨��ṹ������python object��Ҳ���ǵ�������
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
