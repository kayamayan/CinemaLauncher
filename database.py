# encoding:utf-8
from pymongo import MongoClient, ReturnDocument

import json
from bson import ObjectId
from urllib import parse, request

# import user


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


class CinemaDatabase:
    def __init__(self):
        self.client = self.connect_db()
        self.cinema_common = self.client.cinema_common
        self.project_collection = self.cinema_common.projects

    def connect_db(self):
        uri = "mongodb+srv://toribro:Pass_Word_01@cinemadb.ulcqb.mongodb.net/?retryWrites=true&w=majority&appName=CinemaDB"
        client = MongoClient(uri)
        return client

    def insert_db(self, data):
        result = self.project_collection.insert_one(data)

    def update_project(self, data):
        self.project_collection.update_one(
            {'_id': data["_id"]},
            {'$set': data},
            upsert=True
        )
        return True

    def delete_project(self, data):
        self.project_collection.delete_one({'_id': data["_id"]})

    def get_projects(self, include_finished):
        projects_data = self.project_collection.find({}, {"name_korean": 1, "engine_version": 1, "finished": 1})
        projects = []
        for i in projects_data:
            if not include_finished and not i.get("finished", "False"): # 미완료 프로젝트
                projects.append(i["name_korean"] + " (" + i["engine_version"] + ")")
            elif include_finished and i.get("finished", "False"):
                projects.append(i["name_korean"] + " (" + i["engine_version"] + ")")
        return projects

    def get_project_data(self, project):
        datas = self.project_collection.find({'name_korean': project},
                                            {"content_path": 1, "engine_version": 1, "resource_path": 1, "name": 1, "name_korean": 1, "finished": 1})
        result = {}
        for data in datas:
            for k, v in data.items():
                result.update({k: v})
        return result
