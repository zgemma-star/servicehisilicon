#include "servicehisilicon.h"

static PyMethodDef servicehisiliconMethods[] =
{
	 {NULL,NULL,0,NULL}
};

#if PY_MAJOR_VERSION >= 3
	static struct PyModuleDef moduledef = {
		PyModuleDef_HEAD_INIT,
		"servicehisilicon",					/* m_name */
		"Module for servicehisilicon",		/* m_doc */
		-1,									/* m_size */
		servicehisiliconMethods,			/* m_methods */
		NULL,								/* m_reload */
		NULL,								/* m_traverse */
		NULL,								/* m_clear */
		NULL,								/* m_free */
	};
#endif

PyMODINIT_FUNC
initservicehisilicon(void)
{
#if PY_MAJOR_VERSION >= 3
	PyModule_Create(&moduledef);
#else
	Py_InitModule("servicehisilicon", servicehisiliconMethods);
#endif
}
