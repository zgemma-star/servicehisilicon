from . import _
from Components.ActionMap import ActionMap
from Components.Button import Button
from Components.config import config, ConfigSubsection, ConfigYesNo, getConfigListEntry
from Components.ConfigList import ConfigListScreen
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen

config.plugins.servicehisilicon = ConfigSubsection()
config.plugins.servicehisilicon.activate = ConfigYesNo(default=False)

class HisiSetup(ConfigListScreen, Screen):
	skin = """
		<screen name="HisiSetup" position="center,center" size="574,165" title="%s">
			<widget name="config" position="10,10" size="554,100" scrollbarMode="showOnDemand" transparent="1" />
			<widget name="key_red" position="157,121" size="140,40" valign="center" halign="center" zPosition="4" foregroundColor="white" font="Regular;18" transparent="1" /> 
			<widget name="key_green" position="317,121" size="140,40" valign="center" halign="center" zPosition="4" foregroundColor="white" font="Regular;18" transparent="1" /> 
			<ePixmap name="red" position="156,121" zPosition="2" size="140,40" pixmap="buttons/red.png" transparent="1" alphatest="on" />
			<ePixmap name="green" position="317,121" zPosition="2" size="140,40" pixmap="buttons/green.png" transparent="1" alphatest="on" />
		</screen>""" % _("ServiceHisilicon Setup")

	def __init__(self, session, args = 0):
		self.session = session
		Screen.__init__(self, session)

		self.list = []
		self.list.append(getConfigListEntry(_("Enable ServiceHisilicon (Need restart GUI):"), config.plugins.servicehisilicon.activate))

		ConfigListScreen.__init__(self, self.list)

		self["key_red"] = Button(_("Cancel"))
		self["key_green"] = Button(_("Ok"))

		self["setupActions"] = ActionMap(["SetupActions", "ColorActions"],
		{
			"red": self.exit,
			"green": self.save,
			"save": self.save,
			"cancel": self.exit,
			"ok": self.save,
		}, -2)

	def save(self):
		for x in self["config"].list:
			x[1].save()
		self.close(True,self.session)

	def exit(self):
		for x in self["config"].list:
			x[1].cancel()
		self.close()

def main(session, **kwargs):
	session.open(HisiSetup)

def autostart(reason, **kwargs):
	if config.plugins.servicehisilicon.activate.value:
		import servicehisilicon

def Plugins(**kwargs):
	return [
		PluginDescriptor(name = _("ServiceHisilicon Setup"), description = _("Enable/Disable hisilicon libraries for multimedia player."), where = PluginDescriptor.WHERE_PLUGINMENU, icon = "servicehisilicon.png", fnc = main),
		PluginDescriptor(where = PluginDescriptor.WHERE_AUTOSTART, needsRestart = True, fnc = autostart)
	]
