from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url


    def get_project(self):
        # Tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print("Raaka TOML tiedosto")
        print()
        print(content)

        # Käytä toml.loads muuntaaksesi TOML-merkkijono Pythonin tietorakenteeksi
        print("Muutetaan python tietorakenteeksi")
        toml_data = toml.loads(content)
        print()
        print(toml_data)

        # Luo Project-olio annetuista tiedoista
        project = Project(
            name= toml_data.get("tool", {}).get("poetry", {}).get("name", ""),
            license= toml_data.get("tool", {}).get("poetry", {}).get("license", ""),
            authors= toml_data.get("tool", {}).get("poetry", {}).get("authors", []),
            description= toml_data.get("tool", {}).get("poetry", {}).get("description", ""),
            dependencies= toml_data.get("tool", {}).get("poetry", {}).get("dependencies", []),
            dev_dependencies= toml_data.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", []),
        )

        # Tulosta projekti
        print()
        print("Tulostetaan muokattu tietorakenne")
        return project