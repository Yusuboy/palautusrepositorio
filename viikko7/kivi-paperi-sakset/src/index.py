from vs import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_pelaaja_vs_pelaaja import KiviPaperiSakset

def main():
    valinnat = {
        "a": KPSPelaajaVsPelaaja(),
        "b": KPSTekoaly(),
        "c": KiviPaperiSakset()
    }

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input("syote:")

        if vastaus == "a":
            valinta = valinnat[vastaus]
        elif vastaus == "b":
            valinta = valinnat["b"]
        elif vastaus == "c":
            valinta = valinnat["c"]
        else:
            break
        valinta.pelaa()

if __name__ == "__main__":
    main()