from elasticsearch import Elasticsearch
import yaml
from elasticsearch_dsl import Search
import re

# This class connects the code to the Elasticsearch.
class ConnectAndQueryToElasticSearch:

    #-------------------------------------------------------------------------------------------------------------------------    
    def cve_2019_13139(self):
        client = Elasticsearch('https://127.0.0.1:9200', http_auth=('elastic', 'jmDLD_TIBzArUK5ooUH4'), verify_certs=True, ca_certs="/home/kali_cloud/Shafayat_Experiments/INSE_6130/third-party/elasticsearch-8.12.2/config/certs/http_ca.crt",)
        s = Search(using=client, index="cve-2019-13139")
        s = s.query("match", systemcall="execve") # Check system call with execve
        s = s.sort('-@timestamp')
        response = s.execute()

        time_arr = []
        for hit in response:
            arg = hit.arguments.split(',', 1) 
            pattern1 = r'\b\w+\.git\b'
            pattern2 = r'docker build'
            pattern3 = r'-c'
    
            # Find all occurrences of .git in the input string
            match1 = re.findall(pattern1, arg[1])
            match2 = re.findall(pattern2, arg[1])
            match3 = re.findall(pattern3, arg[1])

            # Checking Arguments values
            if arg[0] == '\"/bin/bash\"' and bool(match1)==True:
                time_arr.append(hit.time)
            
            if arg[0] == '\"/usr/bin/docker\"' and bool(match2)==True:
                time_arr.append(hit.time)
            
            if arg[0] == '\"/bin/sh\"' and bool(match3)==True:
                time_arr.append(hit.time)

        if sorted(time_arr, reverse=True) == time_arr:
            print("****Possible CVE-2019-13139****")

        return client
    
    #-------------------------------------------------------------------------------------------------------------------------

    def cve_2024_21626(self):
        
        client = Elasticsearch('https://127.0.0.1:9200', http_auth=('elastic', 'jmDLD_TIBzArUK5ooUH4'), verify_certs=True, ca_certs="/home/kali_cloud/Shafayat_Experiments/INSE_6130/third-party/elasticsearch-8.12.2/config/certs/http_ca.crt",)
        
        s1 = Search(using=client, index="tar_docker")
        s2 = Search(using=client, index="tar_system")
        
        s1 = s1.query("match", systemcall="chdir") # Check system call with execve
        s2 = s2.query("match", systemcall="read") # Check system call with execve
        # s2 = s2.filter('message', tags=['WORKDIR'])


        s1 = s1.sort('-@timestamp')
        s2 = s2.sort('-@timestamp')
        s2cnt = s2.count()

        response1 = s1.execute()
        response2 = s2[0:s2cnt].execute()

        jumpUp = 0
        depthIn = 0

        for hit in response1:
            pattern = r'../../../'
    
            # Find all occurrences of .git in the input string
            match1 = re.findall(pattern, hit.arguments)
            if bool(match1)==True and hit.return_code == '0':
                jumpUp = len(hit.arguments.split('/'))
                break
        # print(len(response2))
        for hit in response2:
            # print(hit.time, hit.arguments)
            pattern = r'.*WORKDIR.*'
            match2 = re.findall(pattern, hit.arguments)
            if bool(match2) == True:
                match2 = match2[0].split('WORKDIR ')[1]
                match2 = match2.split('\\')[0]
                match2 = match2.split('/')[1:]
                depthIn = len(match2)
                break

        if jumpUp >= depthIn:
            print("****Possible CVE-2024-21626****")
            


        # time_arr = []
        # for hit in response:
        #     arg = hit.arguments.split(',', 1) 
        #     pattern1 = r'\b\w+\.git\b'
        #     pattern2 = r'docker build'
        #     pattern3 = r'-c'
    
        #     # Find all occurrences of .git in the input string
        #     match1 = re.findall(pattern1, arg[1])
        #     match2 = re.findall(pattern2, arg[1])
        #     match3 = re.findall(pattern3, arg[1])

        #     # Checking Arguments values
        #     if arg[0] == '\"/bin/bash\"' and bool(match1)==True:
        #         time_arr.append(hit.time)
            
        #     if arg[0] == '\"/usr/bin/docker\"' and bool(match2)==True:
        #         time_arr.append(hit.time)
            
        #     if arg[0] == '\"/bin/sh\"' and bool(match3)==True:
        #         time_arr.append(hit.time)

        # if sorted(time_arr, reverse=True) == time_arr:
        #     print("****Possible CVE-2019-13139****")

        return client
    
    #-------------------------------------------------------------------------------------------------------------------------


    