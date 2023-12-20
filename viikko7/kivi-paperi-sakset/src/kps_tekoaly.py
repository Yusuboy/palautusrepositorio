from tuomari import Tuomari
from tekoaly import Tekoaly
from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly:
    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = Tekoaly()
        while True:
            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            if self._onko_ok_siirto(ekan_siirto) == False:
                break
            tokan_siirto = tekoaly.anna_siirto()
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(f"Tietokone valitsi: {tokan_siirto}")
            print(tuomari)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"