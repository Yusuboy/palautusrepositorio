import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
import random

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 1)
            if tuote_id == 2:
                return Tuote(2, "vesi", 2)
            if tuote_id == 3:
                return Tuote(3, "mehu", 3)
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
    
    def test_osto_valmistuu_pankin_metodi_kutsuu_tilisiirtoon(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")


        self.pankki_mock.tilisiirto.assert_called()



    def test_suorita_ostos_ja_kutsu_pankin_siirto_metodia_oikeilla_argumenteilla(self):
            self.kauppa.aloita_asiointi()
            self.kauppa.lisaa_koriin(1)
            self.kauppa.tilimaksu("pekka", "12345")
     
            self.pankki_mock.tilisiirto.assert_called_with(
                "pekka", ANY, "12345", ANY, 1)

    def test_osta_kaksi_samaa_tuotetta_suorita_tilisiirto_pankkiin_oikeilla_argumenteilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        call_args = self.pankki_mock.tilisiirto.call_args

       
        self.assertEqual(call_args[0][0], "pekka") 
        self.assertEqual(call_args[0][2], "12345")  
        self.assertEqual(call_args[0][4], 2) 

    def test_osta_kaksi_erilaista_tuotetta_suorita_tilisiirto_pankkiin_oikeilla_argumenteilla(self):        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

           
        self.pankki_mock.tilisiirto.assert_called_with(
                "pekka", ANY, "12345", ANY, 1+2)

    
    def test_aloita_uusi_ostos_ja_nollaa_edellisen_ostoksen_tiedot(self):    
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 2
        )

    def test_generoi_uusi_viitenumero_jokaiselle_maksutapahtumalle(self):
        for _ in range(3):
            self.kauppa.aloita_asiointi()
            self.kauppa.lisaa_koriin(1)
            self.kauppa.tilimaksu("pekka", "12345")

            # Tarkastetaan että viitegeneraattoria on kutsuttu odotetusti
            expected_call_count = _ + 1  # 1, 2, 3
            self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, expected_call_count)


    def test_poista_tuote_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
        "pekka", 42, "12345", ANY, 0
        )