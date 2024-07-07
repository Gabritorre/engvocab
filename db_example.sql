-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: engvocabDB
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


--
-- Dumping data for table `vocapp_expression`
--

LOCK TABLES `vocapp_expression` WRITE;
/*!40000 ALTER TABLE `vocapp_expression` DISABLE KEYS */;
INSERT INTO `vocapp_expression` VALUES (1,'Brother-in-law / Sister-in-law','Cognato / Cognata','fratello o sorella del cogniuge, oppure cogniuge del fratello o sorella','Relationship','Mary\'s husband and brother-in-law have also been arrested','Anche il marito di Mary e il cognato sono stati arrestati.',0,0,0,'B1','Noun'),(2,'Nephew','Nipote','Nipote maschio di zii','Relationship','My nephew loves playing soccer. He\'s on the school team.','Mio nipote ama giocare a calcio. Fa parte della squadra scolastica.',0,0,0,'A1/A2','Noun'),(3,'Niece','Nipote','Nipote femmina di zii','Relationship','I bought a special gift for my niece\'s birthday.','Ho comprato un regalo speciale per il compleanno di mia nipote.',0,0,0,'A1/A2','Noun'),(4,'To do overtime','Fare gli straordinari','Lavoro svolto oltre il normale orario di lavoro','Working life','I have to do overtime this weekend to finish this project.','Devo fare gli straordinari questo fine settimana per terminare questo progetto.',0,0,0,'B1+','Idiom'),(5,'To apply for something','Candidarsi per qualcosa, fare richiesta','Spesso usato per richieste di una posizione lavorativa','Working life','She\'s going to apply for a job at the new company in town.','Lei sta per fare domanda per un lavoro presso la nuova azienda in città.',1,0,0,'B1','Idiom'),(6,'Resign','Dimettersi, licenziarsi','lasciare volontariamente una posizione lavorativa, usato in contesti formali','Working life','She decided to resign from her position as manager due to personal reasons.','Ha deciso di dimettersi dalla sua posizione di manager per motivi personali.',0,1,0,'B2','Verb'),(7,'Retire','Andare in pensione','Rinunciare alla posizione lavorativa in età avanzata','Working life','After working for 40 years, John decided to retire and enjoy his well-deserved rest.','Dopo aver lavorato per 40 anni, John ha deciso di ritirarsi e godersi il meritato riposo.',0,0,0,'B1','Verb'),(8,'Coach','Autobus, Corriera, carrozza','Riferito quando il veicolo è specifico per un viaggio turistico, per grandi distanze senza fermate intermedie. Riferito anche alla carrozza dei treni','Travel','We booked seats on the coach for our day trip to the countryside.','Abbiamo prenotato dei posti sull\'autobus per la nostra gita di un giorno in campagna.',0,0,0,'A1/A2','Noun'),(9,'Subway','Metropolitana, sottopassaggio','Sistema di trasporto dove treni viaggiano sottoterra. In alcuni contesti si riferisce semplicemente ad un sottopassaggio','Travel','I take the subway to work every day.','Prendo la metropolitana per andare al lavoro ogni giorno.',0,0,0,'A1/A2','Noun'),(10,'Lorry','Camion, Autocarro','Veicolo usato per il trasporto di merci su strada, sinonimo di \"truck\"','Travel','The lorry was loaded with construction materials for the building site.','Il camion era carico di materiali da costruzione per il cantiere edile.',0,0,0,'B1','Noun'),(11,'Ferry','Traghetto','Imbarcazione usata per il trasporto di veicoli e persone in mare','Travel','We took the ferry from Naples to Capri for a day trip.','Abbiamo preso il traghetto da Napoli a Capri per una gita di un giorno.',0,0,0,'B1+','Noun'),(12,'Revise','Ripassare, studiare, rivedere, riesaminare','Spesso utilizzato per gli esami o compiti. Ma vale anche per progetti, idee, opinioni, ...','Education / working life','In preparation for the final exam, I need to revise for all the topics we\'ve covered in class.','In preparazione per l\'esame finale, devo studiare attentamente tutti gli argomenti che abbiamo affrontato in classe.',0,0,0,'B2','Verb'),(13,'Hand something in','Consegnare un compito / un elaborato','Si intende il gesto fisico di consegnare un lavoro a qualcuno di autorità superiore alla propria','Education / working life','I need to hand in my essay by Friday.','Devo consegnare il mio saggio entro venerdì.',1,0,0,'B1+','Idiom'),(14,'Give a presentation','Tenere una presentazione','Sostenere una presentazione formale o informale di fronte ad un pubblico','Education / working life','I have to give a presentation on the company\'s financial performance at the next board meeting.','Devo fare una presentazione sulle performance finanziarie dell\'azienda alla prossima riunione del consiglio di amministrazione.',0,0,0,'A1/A2','Idiom'),(15,'Nursery','Asilo','Scuola materna per i bambini nei primi anni di vita','Education','I\'m looking for a nursery school for my daughter to attend next year.','Sto cercando una scuola materna a cui mia figlia possa partecipare l\'anno prossimo.',0,0,0,'B2','Noun'),(16,'Attic','Soffitta, attico','Parte della casa che si trova sotto il tetto, usata principalmente come magazzino, non facilmente accessibile dai piani inferiori','House / living spaces','She found an old chest full of treasures in the attic.','Ha trovato una vecchia cassa piena di tesori nella soffitta.',0,0,0,'B1+','Noun'),(17,'Loft','Mansarda','Zona vivibile sotto il tetto, accessibile facilmente dai piani inferiori','House / living spaces','Their apartment has a loft where they set up a cozy reading nook.','Il loro appartamento ha un soppalco dove hanno creato un\'accogliente angolo lettura.',0,0,0,'C1/C2','Noun'),(18,'Basement','Seminterrato, cantina','Parte dell\'edificio costruite sotto il livello del terreno','House / living spaces','They converted their basement into a home theater.','Hanno trasformato il loro seminterrato in un home theater.',0,0,0,'B1+','Noun'),(19,'Fang','Zanna','Grosso e affilato dente di animale quali leone, tigre, leopardo, ecc... (non quelle degli elefanti, chiamate \"tusks\")','Animals / animal parts','The tiger\'s fangs were sharp and intimidating as it approached its prey.','I denti del tigre erano affilati e intimidatori mentre si avvicinava alla sua preda.',0,0,0,'B1+','Noun');
/*!40000 ALTER TABLE `vocapp_expression` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Dumping data for table `vocapp_level`
--

LOCK TABLES `vocapp_level` WRITE;
/*!40000 ALTER TABLE `vocapp_level` DISABLE KEYS */;
INSERT INTO `vocapp_level` VALUES ('A1/A2'),('B1'),('B1+'),('B2'),('C1/C2');
/*!40000 ALTER TABLE `vocapp_level` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Dumping data for table `vocapp_role`
--

LOCK TABLES `vocapp_role` WRITE;
/*!40000 ALTER TABLE `vocapp_role` DISABLE KEYS */;
INSERT INTO `vocapp_role` VALUES ('Adjective'),('Adverb'),('Article'),('Conjunction'),('Idiom'),('Noun'),('Preposition'),('Slang'),('Verb');
/*!40000 ALTER TABLE `vocapp_role` ENABLE KEYS */;
UNLOCK TABLES;



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
