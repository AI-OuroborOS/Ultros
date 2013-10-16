# coding=utf-8
__author__ = 'Sean'


class Channel(object):
    def __init__(self, protocol, channel_id, name, parent, position, links):
        self.protocol = protocol
        self.channel_id = channel_id
        self.name = name
        self.parent = parent
        self.position = position
        self.links = links
        self.users = set()

    def __str__(self):
        return u"%s (%s)" % (self.name, self.channel_id)

    def add_link(self, channel_id):
        if channel_id not in self.links:
            self.links.append(channel_id)

    def remove_link(self, channel_id):
        if channel_id in self.links:
            self.links.remove(channel_id)

    def add_user(self, user):
        self.users.add(user)

    def remove_user(self, user):
        try:
            self.users.remove(user)
        except KeyError:
            #According to PEP8, this is easier to read on two lines <_<
            self.protocol.log.debug(
                "Tried to remove non-existent user \"%s\" from channel \"%s\""
                % (user, self))