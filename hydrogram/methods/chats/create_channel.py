#  Hydrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2023 Dan <https://github.com/delivrance>
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
import hydrogram
from hydrogram import raw
from hydrogram import types


class CreateChannel:
    async def create_channel(
        self: "hydrogram.Client",
        title: str,
        description: str = ""
    ) -> "types.Chat":
        """Create a new broadcast channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            title (``str``):
                The channel title.

            description (``str``, *optional*):
                The channel description.

        Returns:
            :obj:`~hydrogram.types.Chat`: On success, a chat object is returned.

        Example:
            .. code-block:: python

                await app.create_channel("Channel Title", "Channel Description")
        """
        r = await self.invoke(
            raw.functions.channels.CreateChannel(
                title=title,
                about=description,
                broadcast=True
            )
        )

        return types.Chat._parse_chat(self, r.chats[0])