import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        project = data["project"]

        name = project["name"]
        description = project["description"]
        license = project.get("license")

        authors = [author ["name"] for author in project.get("authors", [])]
        dependencies = [d.split(">=")[0] for d in project["dependencies"]]
        dev_dependencies = [d.split(">=")[0] for d in data["dependency-groups"]["dev"]]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, license, authors)
