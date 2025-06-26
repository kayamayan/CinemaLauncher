# encoding:utf-8

from P4 import P4, P4Exception


class P4Cmd:
    CHARSET = ["utf8",
               "utf8-bom",
               "none",
               "auto"]

    def login(self):
        self.p4 = P4()
        self.p4.exception_level = 1
        self.p4.connect()

        self.charsetIndex = self.CHARSET.index(self.p4.charset)

    @staticmethod
    def get_workspace():
        P4Cmd().login()
        client_info = P4Cmd().fetchClient()
        if client_info["Root"] == 'null':
            client = client_info["Client"]
            client_view = client_info["View"]

            root_data = {}
            for view in client_view:
                title = None
                value = None
                if view.startswith('//Resource/...'):
                    title = "resource"
                    value = view.split(client + "/")[1].replace("/Resource/...", "")
                elif view.startswith('//depot/...'):
                    title = "depot"
                    value = view.split(client + "/")[1].replace("/depot/...", "")
                elif view.startswith('//Asset_Library/...'):
                    title = "asset_library"
                    value = view.split(client + "/")[1].replace("/Asset_Library/...", "")
                root_data[title] = value
            return root_data
        else:
            root = client_info["Root"].replace("\\", "/")
        P4Cmd().p4.charset = str(P4Cmd.CHARSET[P4Cmd().charsetIndex])
        return {"resource": root, "depot": root, "asset_library": root}

    @staticmethod
    def get_user():
        client_info = P4Cmd().fetchClient()
        user = client_info["Owner"]
        P4Cmd().p4.charset = str(P4Cmd.CHARSET[P4Cmd().charsetIndex])
        return user

    def __init__(self):
        self.login()

    def get_workspaces(self, user, password):
        workspaces = list()
        self.p4.user = user
        self.p4.password = password
        self.p4.charset = 'utf8'
        try:
            # self.p4.run_login()
            for i in self.p4.run('clients', '-u', user):  # self.p4.user):
                if i["Host"] == self.p4.host:
                    workspaces.append(i["client"])
        except P4Exception as e:
            print(e)
        return workspaces

    def fetchClient(self):
        try:
            client_info = self.p4.fetch_client()
        except P4Exception as e:
            self.p4.charset = str(self.CHARSET[int(not self.charsetIndex)])
            client_info = self.p4.fetch_client()
        return client_info

    def set_user(self, user):
        client_info = self.fetchClient()
        self.p4.user = user
        self.p4.charset = str(self.CHARSET[self.charsetIndex])

    def set_client(self, client):
        client_info = self.fetchClient()
        self.p4.client = client
        self.p4.charset = str(self.CHARSET[self.charsetIndex])

    def set_password(self, password):
        client_info = self.fetchClient()
        self.p4.password = password
        self.p4.charset = str(self.CHARSET[self.charsetIndex])

    def set_charset(self, charset):
        client_info = self.fetchClient()
        self.p4.charset = charset

    def add(self, file):
        client_info = self.fetchClient()
        self.p4.run_add('-d', file)
        self.p4.charset = str(self.CHARSET[self.charsetIndex])

    def checkout(self, file):
        client_info = self.fetchClient()
        self.p4.run_edit(file)
        self.p4.charset = str(self.CHARSET[self.charsetIndex])

    def pull(self, path):
        client_info = self.fetchClient()
        self.p4.run('sync', path + "...#head")
        self.p4.charset = str(self.CHARSET[self.charsetIndex])
