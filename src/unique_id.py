class UniqueID(object):
    _uid = 1
    def __init__(self):
        self._id = self.uid
        self.uid += 1

    # Unique ID count
    @property
    def uid(self):
        """ Return the uid count of Entities instantiated.

        :returns: int

        """
        return self._uid

    @uid.setter
    def uid(self, new_uid):
        """ Set the Entity.uid count of Entities instantiated to the new_uid
        provided. This will generally be used for incrementing the count.

        :param new_uid: The new count of Entities instantiated.
        :type new_uid: int

        """
        self._uid = new_uid

    # Entity ID
    @property
    def id(self):
        """ Return the Unique ID for a specific Entity instance.

        :returns: int

        """
        return self._id
