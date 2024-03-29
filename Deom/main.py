import pymongo
import glob
import requests
import json
from DAO.postgresql import Postgresql
from colorama import Fore
from colorama import Style
import time
from DAO.mongodb import MongoDB
import ast
import argparse
import datetime
REST_API_ADDRESS = None
ENDPOINT = None


#ip = None

def send_request(lecture):
    return json.loads(requests.post(REST_API_ADDRESS + ENDPOINT, files={'file': open(lecture, 'rb')}).content)['project_id']
    #return requests.post(REST_API_ADDRESS + ENDPOINT, files={'file': open(lecture, 'rb')}).json()['project_id']


def check_job_done(project_id):

    pgsql = Postgresql()
    #pgsql = Postgresql(ip)
    return pgsql.get_jobs_done(project_id)

def get_result_file(file_oid):
    mongodb = MongoDB()
    #mongodb = MongoDB(ip)
    file = mongodb.get_doc_mongo(file_oid)
    #print(file)
    return file


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--server_ip', default='localhost')
    parser.add_argument('--port', default='5000')

    args = parser.parse_args()

    #ip = args.server_ip
    REST_API_ADDRESS = 'http://' + args.server_ip + ':' + args.port
    ENDPOINT = '/segmentation'
    ids = []
    files = glob.glob('Dataset/*.mp4')
    for file in files:
        ids.append((send_request(file), file))

    results = []
    while ids:
        for id, video, in ids:
            res = check_job_done(id)
            if res:

                dc = ast.literal_eval(get_result_file(res['result']['oid']).decode('utf-8'))
                #print(dc)
                dc['segments'] = [str(datetime.timedelta(seconds = n)) for n in dc['segments']]
                
                print(f'{Fore.GREEN}Task completed: {Style.RESET_ALL}'  +str(dc))
                results.append({'Video Name': video, 'Segmentation': dc})
                ids.remove((id, video))

        print('Working on Lecture video segmentation. Please wait.....')
        time.sleep(60)
    print('All activity done:')
    print(results)
