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
INSERT INTO `vocapp_expression` VALUES ();
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


--
-- Dumping data for table `vocapp_user`
--

LOCK TABLES `vocapp_user` WRITE;
/*!40000 ALTER TABLE `vocapp_user` DISABLE KEYS */;
INSERT INTO `vocapp_user` VALUES ();
/*!40000 ALTER TABLE `vocapp_user` ENABLE KEYS */;
UNLOCK TABLES;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
