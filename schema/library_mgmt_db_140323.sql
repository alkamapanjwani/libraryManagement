CREATE DATABASE  IF NOT EXISTS `library_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `library_db`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: library_db
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `author` (
  `author_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `is_active_flag` bit(1) NOT NULL DEFAULT b'1',
  PRIMARY KEY (`author_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` VALUES (1,'author 1',_binary ''),(2,'author 2',_binary '\0'),(3,'author 2',_binary ''),(4,'author 3',_binary ''),(5,'J.K. Rowling',_binary ''),(6,'Sevin Okyay',_binary ''),(7,'Mary GrandPré',_binary '');
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `isbn13` varchar(13) NOT NULL,
  `totalqty` int DEFAULT NULL,
  `is_active_flag` bit(1) NOT NULL DEFAULT b'1',
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'1test book','112345',11,_binary ''),(10,'book 2','877',5,_binary ''),(11,'book 3','118989',5,_binary ''),(12,'abc','12345',8,_binary '\0'),(13,'hjkh','12345',8,_binary ''),(14,'test','123457',4,_binary ''),(15,'test','123457',2,_binary ''),(16,'test123','123457890',5,_binary ''),(17,'test123','12345789',5,_binary ''),(18,'test123','1234578',56,_binary ''),(19,'book 34','89899',55,_binary ''),(20,'book 34','8989',5,_binary ''),(21,'Harry Potter ve Sırlar Odası (Harry Potter  #2)','9783570211021',2,_binary ''),(22,'Harry Potter Boxed Set  Books 1-5 (Harry Potter  #1-5)','9780439682589',4,_binary ''),(23,'Harry Potter and the Order of the Phoenix (Harry Potter  #5)','9780439358071',2,_binary ''),(24,'Harry Potter Schoolbooks Box Set: Two Classic Books from the Library of Hogwarts School of Witchcraft and Wizardry','9780439321624',2,_binary '');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_auhor_trans`
--

DROP TABLE IF EXISTS `book_auhor_trans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_auhor_trans` (
  `book_auhor_trans_id` int NOT NULL AUTO_INCREMENT,
  `book_id` int DEFAULT NULL,
  `author_id` int DEFAULT NULL,
  PRIMARY KEY (`book_auhor_trans_id`),
  KEY `fk_book_idx` (`book_id`),
  KEY `fk_book_author_trans_author_idx` (`author_id`),
  CONSTRAINT `fk_book_author_trans_author` FOREIGN KEY (`author_id`) REFERENCES `author` (`author_id`),
  CONSTRAINT `fk_book_author_trans_book` FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_auhor_trans`
--

LOCK TABLES `book_auhor_trans` WRITE;
/*!40000 ALTER TABLE `book_auhor_trans` DISABLE KEYS */;
INSERT INTO `book_auhor_trans` VALUES (3,10,3),(5,11,1),(7,13,1),(8,14,1),(10,15,1),(12,16,1),(13,16,3),(15,17,1),(17,18,1),(23,20,4),(24,16,4),(25,17,4),(26,20,1),(27,19,4),(30,1,1),(31,1,4),(32,21,5),(33,21,6),(34,22,5),(35,22,7),(36,23,5),(37,23,7),(38,24,5);
/*!40000 ALTER TABLE `book_auhor_trans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_issue`
--

DROP TABLE IF EXISTS `book_issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_issue` (
  `book_issue_id` int NOT NULL AUTO_INCREMENT,
  `book_id` int DEFAULT NULL,
  `member_id` int DEFAULT NULL,
  `issue_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `return_date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `is_returned_flag` varchar(3) DEFAULT 'no',
  PRIMARY KEY (`book_issue_id`),
  KEY `fk_book_ssue_book_idx` (`book_id`),
  KEY `fk_book_issue_member_idx` (`member_id`),
  CONSTRAINT `fk_book_issue_book` FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`),
  CONSTRAINT `fk_book_issue_member` FOREIGN KEY (`member_id`) REFERENCES `member` (`member_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_issue`
--

LOCK TABLES `book_issue` WRITE;
/*!40000 ALTER TABLE `book_issue` DISABLE KEYS */;
INSERT INTO `book_issue` VALUES (1,1,1,'2023-03-11 16:20:22','2023-03-12 23:09:59','yes'),(2,1,1,'2023-03-12 23:10:41','2023-03-13 00:34:07','yes'),(5,1,1,'2023-03-13 01:37:36',NULL,'no'),(6,21,1,'2023-03-13 23:13:17',NULL,'no'),(7,21,1,'2023-03-13 23:16:23',NULL,'no'),(8,21,1,'2023-03-13 23:18:48',NULL,'no'),(9,23,6,'2023-03-14 00:11:47',NULL,'no');
/*!40000 ALTER TABLE `book_issue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `member_Id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `is_active_flag` bit(1) NOT NULL DEFAULT b'1',
  PRIMARY KEY (`member_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'alkamaa','alkamarajan@gmail.comk','99302304846',_binary ''),(5,'tetst','hljj','787834',_binary '\0'),(6,'dwq','sf@s.c','024335345345454545454545454555555555555554',_binary ''),(7,'ad','dsa','ads',_binary ''),(8,'k','kj','9',_binary ''),(9,'hgh','hgjh','786',_binary '');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `setting`
--

DROP TABLE IF EXISTS `setting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `setting` (
  `setting_id` int NOT NULL AUTO_INCREMENT,
  `setting_name` varchar(255) DEFAULT NULL,
  `setting_value` int DEFAULT NULL,
  PRIMARY KEY (`setting_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `setting`
--

LOCK TABLES `setting` WRITE;
/*!40000 ALTER TABLE `setting` DISABLE KEYS */;
INSERT INTO `setting` VALUES (1,'outstanding_debt',500),(2,'book_fees',200);
/*!40000 ALTER TABLE `setting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `comment` varchar(1000) DEFAULT NULL,
  `cr_amount` int NOT NULL DEFAULT '0',
  `dr_amount` int NOT NULL DEFAULT '0',
  `date_inserted` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `member_id` int NOT NULL,
  `book_issue_id` int DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `fk_transaction_book_issue_idx` (`book_issue_id`),
  KEY `fk_transaction_member_idx` (`member_id`),
  CONSTRAINT `fk_transaction_book_issue` FOREIGN KEY (`book_issue_id`) REFERENCES `book_issue` (`book_issue_id`),
  CONSTRAINT `fk_transaction_member` FOREIGN KEY (`member_id`) REFERENCES `member` (`member_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (1,'test 1',0,100,'2023-03-13 18:44:26',1,NULL),(2,'test 2',50,0,'2023-03-13 18:44:26',1,NULL),(3,'Book Issued',0,500,'2023-03-13 23:13:17',1,6),(4,'Book Issued',0,100,'2023-03-13 23:16:23',1,7),(5,'Book Issued',0,200,'2023-03-14 00:11:47',6,9),(6,'test 1',100,0,'2023-03-14 00:29:47',1,NULL),(7,'test 2',100,0,'2023-03-14 00:35:55',1,NULL);
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'library_db'
--

--
-- Dumping routines for database 'library_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-14  1:37:31
