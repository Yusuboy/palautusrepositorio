class IntJoukko:
    OLETUS_KAPASITEETTI = 5
    OLETUS_KASVATUSKOKO = 5

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti or self.OLETUS_KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or self.OLETUS_KASVATUSKOKO
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, arvo):
        return arvo in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, arvo):
        if not self.kuuluu(arvo):
            self.ljono[self.alkioiden_lkm] = arvo
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                self._kasvata_joukkoa()

            return True

        return False

    def _kasvata_joukkoa(self):
        uusi_koko = self.alkioiden_lkm + self.kasvatuskoko
        uusi_joukko = self._luo_lista(uusi_koko)
        self._kopioi_listasta_toiseen(self.ljono, uusi_joukko)
        self.ljono = uusi_joukko

    def _kopioi_listasta_toiseen(self, lahde, kohde):
        for i in range(len(lahde)):
            kohde[i] = lahde[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
