# SharedNotes

Sovelluksella käyttäjät voivat luoda jaettuja muistiinpanoja. Käyttäjä voi jakaa muistiinpanon useamman käyttäjän kanssa. Muistiinpanohin voi lisätä alimuistiinpanoja. 

Tietokantakaavio: [Linkki](https://github.com/asiikaluoma/SharedNotes/blob/master/dokumentaatio/tietokantakaavio.png)

## Käyttäjät

Muistiinpanon luonut käyttäjä on pääkäyttäjä. Pääkäyttäjä on ainoa joka voi poistaa muistiinpanon. Muistiinpanon poisto poistaa myös kaikki alimuistiinpanot. Jaetut käyttäjät voivat lisätä alimuistiinpanoja, muokata alimuistiinpanoja ja poistaa itse luomansa alimuistiinpanot. 

Päämuistiinpano sisältää otsikon, kuvauksen sekä listauksen alimuistiinpanoista. Alimuistiinpano sisältää otsikon sekä rungon (teksti, otsikot, yms...) 

Päämuistinpanon tiedoissa näytetään: alimuistiinpanojen lukumäärä, keskiverto merkkien määrä, viimeksi muokattu, käyttäjät.


## Jatkokehitys

Muistiinpanojen versiointi eli voidaan katsella muutoshistoriaa. # SharedNotes
