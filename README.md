Sentiment analyssis from social media
==============================
![sentiment](figures/sentiment-fig.jpg)

Project Organization
------------
    
    ├── app                	 <- link to the application running on heroku 
    │
    ├── dataset            	 <- datasets
    │
    ├── figures            	 <- Generated figures  
    │
    ├── notebooks          	 <- Jupyter notebooks 
    │   ├── src
    │       ├── TwitterScraper  <- Code for scraping twitter tweets
   
--------

Målene

Hoved målene i dette prosjektet var for meg å få erfaring med NLP teknikker ved hjelp av Fastai biblioteket. 

Hva har jeg gjort

Steg 1

Det jeg startet med var se Fastai sinn forelesning om NLP, leste kapittel 10 og gikk gjennom tilhørende notebook. Dette ga en grei introduksjon for hvordan man kan gjøre sentiment analyse ved hjelp av Fastai biblioteket.  

Etter dette prøvde jeg denne fremgangsmåten på et par datasett for å se hvor gode resultater jeg kunne få. Koden for dette ligger i notebook 1 og 2. 

Steg 2

Neste steg jeg ønsket å utforske var å hente data fra Twitter og gjøre sentiment analyse på disse dataene. Her prøvde jeg først å bruke Selenium som scraper tweets ved å automatisere browseren(Notebook 3). Dette fungerte bra, men var litt stress å sette opp siden man måtte inn å finne riktige divs som inneholdt de dataene jeg ønsket å hente ut. Selv om dette fungerte bra og jeg fikk hentet ned masse tweets var det et stort minus at mye av tweetsen ikke kunne brukes, siden de kunne være på alle mulige språk. Dette førte til at jeg begynte å se nærmere på Twitters Developer API og tweepy.

Ved å lage en bruker på Twitters developer portal får man tilgang til apiet deres gjennom noen API nøkkler. Ved å bruke Tweetpy, som er et Python-bibliotek for å aksessere Twitters API, kunne jeg enkelt sette opp og hente tweets. Dette var mye enklere å sette opp en Selenium og hadde mer mulighet for å filetere data etter språk, og man kunne kombinere hashtags osv. 

Etter å ha fått til å hente tweets fra twitter følte jeg at det kunne vært naturlig å prøve å lage sitt eget datasett. Dette skulle vise seg å ikke vær så enkelt og det var her jeg først begynte å få litt problemer.

Det første jeg begynte å utforske i denne prosessen var måter jeg kunne gi labels til de dataene jeg hentet ned. I oppgave teksten var det tipset om et bibliotek som hette snorkel. Snorkel gir oss mulighet til å skrive labeling funksjoner som hjelper oss med å automatisere prosessen med å gi labels til dataene våre. Etter å ha lest litt i dokumentasjonen og gått gjennom noen tutorials var jeg klar for å prøve å lage mitt eget datasett.

Tilbake til å scrape tweets med Twitters api og tweepy (Notebook 4) satt jeg opp en funksjon som skulle hente tweets og skrive disse til en csv fil. Alt virket som det fungerte i starten, men etter en stund krasjet alt og jeg fikk ikke det til å kjøre igjen. Etter en stund virket det igjen. Dette gjentok seg gang på gang. Hver gang det krasjet hadde jeg hentet rundt 2000 tweets. Det tok lengre tid en jeg er komfortabel med å innrømme og finne grunnen til dette, men kort forklart så forsto jeg det slik at twitter sitt API har ett tak på hvor mange request man kan sende hvert 15min. Dette var litt demotiverende og fikk meg til å legge iden om å lage ett eget datasett fra meg og jeg begynte å se på det neste jeg ønsket å få til i dette prosjektet.

Steg 3

Helt siden Dat158, hvor jeg ble introdusert for maskinlære har maskinlære og programvareutvikling stått litt på hvert sinn side i rommet uten at jeg har hatt mulighet til å koble de sammen. Derfor satte jeg meg som mål at jeg skulle deploye en full-stack applikasjon. Planen var at applikasjonen skulle bruke en modell laget av det datasettet jeg selv hadde konstruert. Siden jeg ikke hadde fått dette til måtte jeg finne en annen løsning. 

Etter litt søking på google kom jeg frem til ett bibliotek kalt TextBlob som er et bibliotek for tekst prosessering deriblant sentiment analyse og klassifisering. Jeg fant også en guide for hvordan man kunne bruke TextBlob sammen med tweetpy. Bare med noen få endringer på denne koden kunne jeg tilpasse det slik at dette ble back-end delen av applikasjonen. Koden finner du i notebook 5.

Neste steg var å finne ut hvordan front end og back end skulle kommuniser seg imellom. Her kom jeg over et bibliotek i Python kalt Flask. Flask gjøre det mulig å sette opp et REST api i Phyton som enkelt kan kalles med fetch eller axios fra front end. Koden for dette finnes her https://github.com/Orjanen/Sentiment-flask-backend.

For front-end har valgte jeg å bruke React.js. Trenger ikke gå i detaljer på dette, men bruker semantic ui for å style komponenter og standard biblioteket fetch for å sende http requests. Koden for dette finnes her https://github.com/Orjanen/dat255-sentiment-app

Siste del i denne prosessen var å deploye applikasjonen på en skytjeneste. Jeg valgte å bruke Heroku. React applikasjonen var det ingen problem med å få på nett. Flask applikasjonen var det litt mer styr med. For det første trengte jeg en å ha tilgang til API nøklene mine uten at jeg viste disse for andre. Her brukte jeg Heroku sinn config Vars for å lagre de sikkert, og så bare hentet jeg disse i applikasjonen. Det neste så måtte var å lage en requiements fil, som forteller serveren alle bibliotekene den skal installere slik at den kan kjøre applikasjonen. Dette tok en del tid, siden jeg ikke helt vist hva som var feil når serveren krasjet, men fant ut av det etter hvert. 

Applikasjonen er live på https://sentiment-react.herokuapp.com, legg merke til at Heroku sine dyno bruker litt tid på å våkne, både når man åpner nettsiden førest gang og sender første kallet til back-end. 

Applikasjonen er veldig enkel å gjøre ikke noe fantastisk, men den virker på denne måten. Du skriver inn et brukernavn du ønsker å søke på. Dette blir så sendt til back-end, hvor den bruker tweetpy for å hente de nyeste tweetsene til denne brukeren. Når den har hentet disse gjøres det sentiment analyse på hver tweet som så sendes tilbake til deg.


Steg 4

Den siste tingen jeg har sett litt på er å bruke Vaex istedenfor pandas for å laste inn data (Notebook 6, pre-prosesserer et datasett og gjør det om til hdf5 format). Dette har jeg ikke hatt så mye tid til å se på, og har blitt stående fast når jeg prøver å laste dataene inn i Fastai sin textDataLoader. 

Oppsummering

For min del har dette vært et lærerikt prosjekt. Jeg har kanskje ikke klart å skape noe fantastisk av verdi når det kommer til en model eller et produkt, men jeg føler jeg sitter igjen med mye erfaring som kan bli nyttig senere. 

Jeg har gjennomført sentiment analyse ved hjelp av Fastai og deres fremgangsmåte. Jeg har utforsket hvordan jeg kan lage et eget datasett og lable disse og opplevde problemer som kan oppstå. Det har også blitt laget en enkel applikasjon som kan hente tweets og gjøre sentiment analyse på disse. Jeg har også sett nærmere på måter å håndtere større datamengder. 

Refleksjon

Dersom jeg skulle gjort prosjektet på nytt hadde jeg ønsket og gjort noen endringer. 

Først av alt hadde jeg fokusert mer på dette med sentiment analyse og utforsket flere datasett. Ikke minst prøvde å starte helt fra bunnen av og ikke bruke transfer Learning. Jeg hadde også laget meg en bedre plan, med klarerer mål på hva det er jeg har ønsket å oppnå med dette prosjektet. 

Når jeg ikke klarte å hente ned stor nok mengde tweets til at jeg følte det kunne brukes til å lage et datasett, kunne jeg bare droppe heile greiene og fokusert på noe annet med en gang, isteden for å bruke mye tid på noe jeg ikke fikk til. En annen ting jeg kunne gjort var å bare finne et stort datasett, fjernet alle labelsene og sett om jeg klarte og lable det selv igjen, ved hjelp av snorkel.

Jeg hadde ønsket å bruke mer tid på å forstå hva som ligget bak alt som skjer i Fastai. Grunnen til dette er at jeg har fått som inntrykk at Fastai fungerer veldig bra på de eksemplene som de viser, men som snart man bruker egne data eller annen type data så krever det en del mer forståelse for å få det til å virke like bra. 


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
