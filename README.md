# SharedNotes

Sovelluksella käyttäjät voivat luoda jaettuja muistioita, jotka sisältävät useita muistiinpano. Käyttäjä voi jakaa muistion useamman käyttäjän kanssa. Muistioihin lisätään muistiinpanoja. 

Tietokantakaavio: [Linkki](https://github.com/asiikaluoma/SharedNotes/blob/master/dokumentaatio/tietokantakaavio.png)

Sovellus Herokussa: [Linkki](https://shared-notes.herokuapp.com)

Käyttäjä: testi
Salasana: testi

## Käyttötapaukset

### Käyttöoikeudet

- Muistion luonut käyttäjä on sen omistaja. 
- Omistaja on ainoa joka voi poistaa muistion. 
- Muistion poisto poistaa myös kaikki muistiinpanot. 
- Käyttäjät joille jaettiu oikeudet voivat lisätä muistiinpanoja, muokata muistiinpanoja ja poistaa itse lehtiöön luomansa muistiinpanot. 

### Ominaisuudet

- Kirjautuneen käyttäjän etusivulla listaus muistioista sekä niiden alla listaus niihin kuuluvista viimeisimmistä muistiinpanoista (max. 10).
- Muistiota klikkaamalla päästään sen näkymään
- Näkumä sisältää otsikon, kuvauksen sekä listauksen muistiosta. 
- Kentät ovat muokattavissa omistajan toimesta
- Näkymän tiedoissa näytetään myös: musitiinpanojen lukumäärä, keskiverto merkkien määrä, viimeksi muokattu, käyttäjät
- Kaikki listauksesta ovat lajiteltu viimeisen muokkauksen mukaan
- Muistiinpanolistauksesta siirrytään muistiinpanoa kliikkammalla sen omaan näkymään
- Kentät ovat muistiinpanon näkymässä muokattavissa
- Itse muistiinpano sisältää otsikon sekä rungon (teksti, otsikot, yms...).

## Jatkokehitys

Muistiinpanojen versiointi eli voidaan katsella muutoshistoriaa.
