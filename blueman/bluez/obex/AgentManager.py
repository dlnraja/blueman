# coding=utf-8
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

from blueman.Functions import dprint
from blueman.bluez.obex.Base import Base
from gi.repository import GLib

class AgentManager(Base):
    _interface_name = 'org.bluez.obex.AgentManager1'

    def _init(self):
        super(AgentManager, self)._init(interface_name=self._interface_name, obj_path='/org/bluez/obex')

    def register_agent(self, agent_path):
        def on_registered():
            dprint(agent_path)

        def on_register_failed(error):
            dprint(agent_path, error)

        param = GLib.Variant('(o)', (agent_path,))
        self._call('RegisterAgent', param, reply_handler=on_registered, error_handler=on_register_failed)

    def unregister_agent(self, agent_path):
        def on_unregistered():
            dprint(agent_path)

        def on_unregister_failed(error):
            dprint(agent_path, error)

        param = GLib.Variant('(o)', (agent_path,))
        self._call('UnregisterAgent', param, reply_handler=on_unregistered, error_handler=on_unregister_failed)
