import tomli
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        data = tomli.loads(content)
        
        project = data["project"]
        dev_dependencies = data["dependency-groups"]["dev"]
        authors = [author["name"] for author in project["authors"]]

        return Project(
            project["name"],
            project["description"],
            project["dependencies"],
            dev_dependencies,
            project["license"],
            authors
        )