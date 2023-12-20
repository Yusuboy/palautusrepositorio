from tuomari import Tuomari

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()
        while True:
            ekan_siirto = self.siirto_eka()
            if self._onko_ok_siirto(ekan_siirto) == False:
                break
            tokan_siirto = self.siirto_toka()
            if self._onko_ok_siirto(tokan_siirto) == False:
                break
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def siirto_eka(self):
        siirto = input("Ensimmäisen pelaajan siirto: ")
        return siirto
    
    def siirto_toka(self):
        return input("Toisen pelaajan siirto: ")