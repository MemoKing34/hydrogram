#  Hydrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2020-present Cezar H. <https://github.com/usernein>
#  Copyright (C) 2023-present Amano LLC <https://amanoteam.com>
#
#  This file is part of Hydrogram.
#
#  Hydrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Hydrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Hydrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Optional

import hydrogram
from hydrogram.types import Identifier, Listener, ListenerTypes


class GetListenerMatchingWithIdentifierPattern:
    def get_listener_matching_with_identifier_pattern(
        self: "hydrogram.Client", pattern: Identifier, listener_type: ListenerTypes
    ) -> Optional[Listener]:
        """
        Gets a listener that matches the given identifier pattern.

        The difference from :meth:`hydrogram.Client.get_listener_matching_with_data` is that this method
        intends to get a listener by passing partial info of the listener identifier, while the other method
        intends to get a listener by passing the full info of the update data, which the listener should match with.

        Parameters:
            pattern (:obj:`~hydrogram.types.Identifier`):
                The identifier pattern to match against.

            listener_type (:obj:`~hydrogram.types.ListenerTypes`):
                The type of listener to get.

        Returns:
            :obj:`~hydrogram.types.Listener`: The listener that matches the given identifier pattern or ``None`` if no listener matches.
        """
        matching = [
            listener
            for listener in self.listeners[listener_type]
            if pattern.matches(listener.identifier)
        ]

        # in case of multiple matching listeners, the most specific should be returned

        def count_populated_attributes(listener_item: Listener):
            return listener_item.identifier.count_populated()

        return max(matching, key=count_populated_attributes, default=None)
