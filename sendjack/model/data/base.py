"""

    base
    ----

    Provide abstract database access.

"""


class Database(object):


    def __init__(self, tables_list):
        self._set_up_db()


    def _set_up_db(self):
        print 'OverrideRequiredError'
        # raise OverrideRequiredError()
