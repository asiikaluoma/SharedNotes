# SharedNotes

Sovelluksella käyttäjät voivat luoda jaettuja muistioita, jotka sisältävät useita muistiinpano. Käyttäjä voi jakaa muistion useamman käyttäjän kanssa. Muistioihin lisätään muistiinpanoja. 

Tietokantakaavio: [Linkki](https://github.com/asiikaluoma/SharedNotes/blob/master/dokumentaatio/tietokantakaavio.png)

Sovellus Herokussa: [Linkki](https://shared-notes.herokuapp.com)

Käyttäjä: testi
Salasana: testi

## Käyttötapaukset

### Käyttöoikeudet

- Muistion luonut käyttäjä on sen omistaja. 
- Omistaja on ainoa, joka voi lisätä oikeuksia muille käyttäjille.
- Omistaja on ainoa joka voi poistaa muistion. 
- Muistion poisto poistaa myös kaikki muistiinpanot. 
- Käyttäjä jolle on jaettu oikeudet voi lisätä, muokata ja poistaa muistiinpanoja, mutta vain omista voi muokata muistion tietoja.

### Ominaisuudet

- Kirjautuneen käyttäjän etusivulla listaus muistioista, jokta hän on luonut tai joihin hänet on lisätty
    - Listauksessa näytetään muistion nimi, kuvaus, käyttäjät, viimeisin muokkauspäivä
- Muistiota klikkaamalla pääsee sen näkymään
    - Näkumä sisältää otsikon, kuvauksen sekä listauksen muistiosta. 
    - Näkymä sisältää nappulan, jota klikkaamalla päästään muokkaamaan muistion tietoja
    - Muistion tietojen lisäksi voidaan lisätä muille käyttäjille oikeuksia
- Kaikki listauksesta ovat lajiteltu viimeisen muokkauksen mukaan
- Muistiinpanolistauksesta siirrytään muistiinpanoa kliikkammalla sen omaan näkymään
    - Muistiinpanon näkymä sisältää nappulan, josta päästään muokkaamaan.
- Itse muistiinpano sisältää otsikon sekä rungon (teksti, väliotsikot, yms...).

## Jatkokehitys

Muistiinpanojen versiointi eli voidaan katsella muutoshistoriaa.
