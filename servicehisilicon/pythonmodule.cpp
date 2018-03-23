#include "servicehisilicon.h"


static PyMethodDef servicehisiliconMethods[] =
{
	 {NULL,NULL,0,NULL}
};

PyMODINIT_FUNC
initservicehisilicon(void)
{
	Py_InitModule("servicehisilicon", servicehisiliconMethods);
}
