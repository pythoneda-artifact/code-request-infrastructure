"""
pythoneda/artifact/code_request/infrastructure/dbus/code_request_dbus_signal_emitter.py

This file defines the CodeRequestDbusSignalEmitter class.

Copyright (C) 2023-today rydnr's pythoneda-artifact/code-request-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import BusType
from pythoneda.infrastructure.dbus import DbusSignalEmitter
from pythoneda.shared.artifact_changes.events import ChangeStaged
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import DbusChangeStaged
from typing import Dict

class CodeRequestDbusSignalEmitter(DbusSignalEmitter):

    """
    A Port that emits events relevant to code requests, as d-bus signals.

    Class name: CodeRequestDbusSignalEmitter

    Responsibilities:
        - Connect to d-bus.
        - Emit code request events as d-bus signals.

    Collaborators:
        - pythoneda.application.PythonEDA: Requests emitting events.
        - pythoneda.shared.artifact_changes.events.infrastructure.dbus.DbusChangeStaged
    """
    def __init__(self):
        """
        Creates a new CodeRequestDbusSignalEmitter instance.
        """
        super().__init__()

    def signal_emitters(self) -> Dict:
        """
        Retrieves the configured event emitters.
        :return: For each event, a list with the event interface and the bus type.
        :rtype: Dict
        """
        result = {}
        key = self.__class__.full_class_name(ChangeStaged)
        result[key] = [ DbusChangeStaged, BusType.SYSTEM ]

        return result
