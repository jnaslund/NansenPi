__author__ = 'barba'
import pingdom as pingdomApi

class PingdomService(object):
    def __init__(self, username, password, useremail, api_key):
        self.username = username
        self.password = password
        self.useremail = useremail
        self.pingdomConnection = pingdomApi.PingdomConnection(self.username, self.password, api_key, self.useremail)

    def get_all_sites(self):
        checks = self.pingdomConnection.get_all_checks()
        return checks
    def get_site_by_id(self, id):
        check = self.pingdomConnection.get_check(id)
        return check



