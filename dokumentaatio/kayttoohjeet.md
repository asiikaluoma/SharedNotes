## Käyttöohjeet

### Kirjautuminen ja rekisteröityminen

![Kirjautuminen](https://github.com/asiikaluoma/SharedNotes/blob/master/dokumentaatio/images/login_view.png)

Sovelluksen kaikki toiminnallisuus vaatii kirjautumista. Jos käyttäjä ei ole kirjautunut, hänet ohjataan kirjatumissivulle. Rekisteröityminen on yksinkertaista. Näkymään pääsee navigaation palkin oikeasta reunasta. Rekisteröityessä kysytään nimi, käyttäjätunnus sekä salasana. Käyttäjätunnusta ja salasanaa käytetään kirjautumiseen.

Kirjautumisen jälkeen navigaatiopalkin oikeasta yläkulmasta löytyy aina "Log out" -linkki, jonka avulla onnistuu ulos kirjautuminen. Lisäksi palkista löytyy pikalinkit muistioiden listaamiseen sekä uuden muistion luomiseen.

### Kotinäkymä

![Kotinäkymä](https://github.com/asiikaluoma/SharedNotes/blob/master/dokumentaatio/images/home_view.png)

Kirjautuneen käyttäjän kotinäkymä sisältää listauksen muistiinpanoista, jotka hän on luonut tai joihin hänellä on oikeudet. Muistiota pääsee tarkastelemeen "Open notebook" -nappulasta. Lisäksi "Check statistics" -nappulasta päästään tarkastelemeen muistiohin liittyviä tietoja.

### Muistion näkymä

![Muistion näkymä](https://github.com/asiikaluoma/SharedNotes/blob/master/dokumentaatio/images/notebook_view.png)

Näkymä sisältää listauksen kyseiseen muistioon littyvistä muistiinpanoista sekä muistion nimen alla on nappeja.

#### Napit

- "Back" napista siirrytään takaisin kotinäkymään.
- "Add note" napista siirrytän luomaan uusia muistiinpanoja.
- "Edit notebook" napista päästään muokkaamaan muistion tietoja sekä hallitsemaan käyttäjiä.
- "Delete" nappi poistaa muistion sekä kaikki siihen liittyvät muistiinpanot.

"Edit notebook" sekä "Delet" napit ovat näkyvissä vain muistion omistajalle.

#### Listaus

Listauksessa on jokaisen muistiinpanon osalta siihen linkki "Open". Jokaisessa elementissä on myös otsikko, sisällöstä ensimmäiset 100 merkkiä, viimeinen muokkauspäivä, sen luoneen käyttäjän nimi ja "Delete" -nappula, josta sen voi poistaa.


### Muistion muokkausnäkymä

![Muokkausnäkymä](https://github.com/asiikaluoma/SharedNotes/blob/master/dokumentaatio/images/edit_notebook_view.png)

Näkymässä voi muokata otsikkoa sekä kuvausta. Lisäksi käyttäjille voi lisätä oikeuksia "Enter username" -kentästä. Kenttä hyväksyy vain olemassaolevat käyttäjätunnukset. 