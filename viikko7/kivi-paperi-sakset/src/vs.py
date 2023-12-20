from tuomari import Tuomari


class KPSPelaajaVsPelaaja:
    def pelaa(self):
        tuomari = Tuomari()

        while True:
            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            if self._onko_ok_siirto(ekan_siirto) == False:
                break
            tokan_siirto = input("Toisen pelaajan siirto: ")            
            if self._onko_ok_siirto(tokan_siirto) == False:
                break
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"