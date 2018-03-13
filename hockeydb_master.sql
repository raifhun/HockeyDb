-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: hockeydb
-- ------------------------------------------------------
-- Server version	5.7.18-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `master`
--

DROP TABLE IF EXISTS `master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `master` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(25) DEFAULT NULL,
  `coachID` varchar(25) DEFAULT NULL,
  `hofID` varchar(25) DEFAULT NULL,
  `firstName` varchar(25) DEFAULT NULL,
  `lastName` varchar(25) DEFAULT NULL,
  `nameNote` varchar(50) DEFAULT NULL,
  `nameGiven` varchar(50) DEFAULT NULL,
  `nameNick` varchar(50) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `shootCatch` varchar(50) DEFAULT NULL,
  `legendsID` varchar(20) DEFAULT NULL,
  `ihdbID` int(11) DEFAULT NULL,
  `hrefID` varchar(25) DEFAULT NULL,
  `firstNHL` int(11) DEFAULT NULL,
  `lastNHL` int(11) DEFAULT NULL,
  `firstWHA` int(11) DEFAULT NULL,
  `lastWHA` int(11) DEFAULT NULL,
  `pos` varchar(5) DEFAULT NULL,
  `birthYear` int(11) DEFAULT NULL,
  `birthMon` int(11) DEFAULT NULL,
  `birthDay` int(11) DEFAULT NULL,
  `birthCountry` varchar(25) DEFAULT NULL,
  `birthState` varchar(25) DEFAULT NULL,
  `birthCity` varchar(25) DEFAULT NULL,
  `deathYear` int(11) DEFAULT NULL,
  `deathMon` int(11) DEFAULT NULL,
  `deathDay` int(11) DEFAULT NULL,
  `deathCountry` varchar(25) DEFAULT NULL,
  `deathState` varchar(5) DEFAULT NULL,
  `deathCity` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7762 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-12 18:25:05
