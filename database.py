# encoding:utf-8
from pymongo import MongoClient, ReturnDocument

import json
# from bson import ObjectId
from urllib import parse, request

import user


class VtDatabaseWeb:
    server_address = "http://vaalt/project/"

    def __init__(self):
        pass

    def get_all_data(self):
        data_string = request.urlopen(self.server_address).read()
        data = json.loads(data_string)
        return data

    def update_project_db(self, data: dict):
        # project_data = self.get_project_data(data['name_korean'])
        # data.update({'_id': project_data['_id'] if project_data else None})
        post_data = parse.urlencode(data).encode('utf-8')
        req = request.Request(self.server_address, data=post_data)
        resp = request.urlopen(req)
        return resp

    def get_projects(self, include_finished):
        datas = self.get_all_data()
        result = {}
        for data in datas:
            finished = eval(data.get("finished", "False"))
            if finished and not include_finished:
                continue
            result[data["name_korean"] + " (" + data["engine_version"] + ")"] = data["_id"]["$oid"]
        return result

    def get_project_data(self, project):
        datas = self.get_all_data()
        result = {}
        for data in datas:
            if data["name_korean"] == project:
                data.update({"_id": data["_id"]["$oid"]})
                for k in data.keys():
                    result.update({k: data[k]})
                break
        return result


class VtDatabase:
    def __init__(self):
        self.client = self.connect_db()
        self.main_db = self.client.maindb
        self.project_collection = self.main_db.projects

    def connect_db(self):
        client = MongoClient("172.19.217.80",
                             username=user.get_user(),
                             password=user.get_password(),
                             authSource='admin')
        return client

    def insert_db(self, data):
        result = self.project_collection.insert_one(data)

    def update_project(self, project, data):
        self.project_collection.update_one(
            {'name': project},
            {'$set': data},
            upsert=True
        )

    def get_projects(self):
        projects_data = self.project_collection.find({}, {"name_korean": 1, "engine_version": 1})
        projects = [i["name_korean"] + " (" + i["engine_version"] + ")" for i in projects_data]
        return projects

    def get_project_data(self, project):
        data = self.project_collection.find({'name_korean': project},
                                            {"content_path": 1, "engine_version": 1, "resource_path": 1, "name": 1})
        return data
