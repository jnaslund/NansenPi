import argparse
from services.pingdom import *
__author__ = 'barba'
appMode = 'dev'

def init():
    parser = argparse.ArgumentParser(description='Script monitoring Pingdom and other fun stuff')
    parser.add_argument('-m', '--mode', help='Mode, use \"rbp\" to activate GPIO functionality', required=False)
    args = parser.parse_args()
    global appMode

    if args.mode:
        appMode = args.mode



def getSingle(ps, siteId):
    site = ps.get_site_by_id(siteId)
    print("id: {0}\n, site: {1}, host: {2}, status: {3}".format(site.id, site.name, site.hostname, site.status))

def getall(ps):
    sites = ps.get_all_sites()
    for site in sites:
        print("id: {0}, site: {1}, host: {2}, status: {3}".format(site.id, site.name, site.hostname, site.status))

init()
api_key = ''
username = ''
accountEmail = ''
password = ''
ps = PingdomService(username, password, accountEmail, api_key)
getSingle(ps,'1254382')
#getall(ps)