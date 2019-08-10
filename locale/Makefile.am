LANGS = es
LANGMO = $(LANGS:=.mo)
LANGPO = $(LANGS:=.po)

EXTRA_DIST = $(LANGPO)

.po.mo:
	$(MSGFMT) -o $@ $<

BUILT_SOURCES = $(LANGMO)

dist-hook: $(LANGPO)

install-data-local: $(LANGMO)
	for lang in $(LANGS); do \
		$(mkinstalldirs) $(DESTDIR)${libdir}/enigma2/python/Plugins/SystemPlugins/ServiceHisilicon/locale/$$lang/LC_MESSAGES; \
		$(INSTALL_DATA) $$lang.mo $(DESTDIR)${libdir}/enigma2/python/Plugins/SystemPlugins/ServiceHisilicon/locale/$$lang/LC_MESSAGES/ServiceHisilicon.mo; \
	done

uninstall-local:
	for lang in $(LANGS); do \
		$(RM) $(DESTDIR)${libdir}/enigma2/python/Plugins/SystemPlugins/ServiceHisilicon/locale/$$lang/LC_MESSAGES/ServiceHisilicon.mo; \
	done
