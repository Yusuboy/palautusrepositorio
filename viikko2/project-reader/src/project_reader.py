from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # Tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print("raaka TOML tiedosto:")
        print(content)

        # Käytä toml.loads muuntaaksesi TOML-merkkijono Pythonin tietorakenteeksi
        project_data = toml.loads(content)
        print("\muokattu python tietorakenteeksi:")
        print(project_data)

        # Palauta käsitelty projektitieto
        return project_data