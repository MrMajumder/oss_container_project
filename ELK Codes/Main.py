from ConnectToElasticSearchAndQuery import ConnectAndQueryToElasticSearch

class Main():

    #-------------------------------------------------------------------------------------------------------------------------
    def checkConnection(self):
        objectForConnectToElasticSearchAndQuery = ConnectAndQueryToElasticSearch()
        client = objectForConnectToElasticSearchAndQuery.cve_2024_21626()#cve_2019_13139()
        # print(client)
        # objectForConnectToElasticSearchAndQuery.cve_2019_13139(client)
        # Check if elasticsearch is running or not. If running query in the elasticsearch.
        # if not client.ping():
        #     raise ValueError("Connection failed!")
        # else:
        #     print("Connected...Yipee!!")
        return client

    #-------------------------------------------------------------------------------------------------------------------------
    def run(self):
        self.checkConnection()

    #-------------------------------------------------------------------------------------------------------------------------

mainObj = Main()
mainObj.run()
