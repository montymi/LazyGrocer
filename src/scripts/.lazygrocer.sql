-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (x86_64)
--
-- Host: 127.0.0.1    Database: lazygrocer
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `Favorite`
--

DROP TABLE IF EXISTS `Favorite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Favorite` (
  `recipe_title` varchar(50) DEFAULT NULL,
  `date_added` date DEFAULT NULL,
  `description` text,
  KEY `recipe_title` (`recipe_title`),
  CONSTRAINT `favorite_ibfk_1` FOREIGN KEY (`recipe_title`) REFERENCES `Recipe` (`title`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Favorite`
--

LOCK TABLES `Favorite` WRITE;
/*!40000 ALTER TABLE `Favorite` DISABLE KEYS */;
INSERT INTO `Favorite` VALUES ('Pizza','2024-04-17','Its grown on me'),('Mac','2024-04-17','Incredible dish, would recommend');
/*!40000 ALTER TABLE `Favorite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GroceryList`
--

DROP TABLE IF EXISTS `GroceryList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `GroceryList` (
  `name` varchar(50) NOT NULL,
  `description` text,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GroceryList`
--

LOCK TABLES `GroceryList` WRITE;
/*!40000 ALTER TABLE `GroceryList` DISABLE KEYS */;
INSERT INTO `GroceryList` VALUES ('Busy Week','For when time is running low'),('GL2','For pizza');
/*!40000 ALTER TABLE `GroceryList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ILforI`
--

DROP TABLE IF EXISTS `ILforI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ILforI` (
  `grocery_list_name` varchar(50) DEFAULT NULL,
  `ingredient_name` varchar(50) DEFAULT NULL,
  KEY `grocery_list_name` (`grocery_list_name`),
  KEY `ingredient_name` (`ingredient_name`),
  CONSTRAINT `ilfori_ibfk_1` FOREIGN KEY (`grocery_list_name`) REFERENCES `GroceryList` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ilfori_ibfk_2` FOREIGN KEY (`ingredient_name`) REFERENCES `Ingredient` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ILforI`
--

LOCK TABLES `ILforI` WRITE;
/*!40000 ALTER TABLE `ILforI` DISABLE KEYS */;
INSERT INTO `ILforI` VALUES ('GL2','Dough'),('GL2','Mozzarella Cheese'),('Busy Week','Parmesan Cheese');
/*!40000 ALTER TABLE `ILforI` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ingredient`
--

DROP TABLE IF EXISTS `Ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ingredient` (
  `name` varchar(50) NOT NULL,
  `last_added` date DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ingredient`
--

LOCK TABLES `Ingredient` WRITE;
/*!40000 ALTER TABLE `Ingredient` DISABLE KEYS */;
INSERT INTO `Ingredient` VALUES ('Ambrosia','2024-04-17'),('Black Pepper','2024-04-17'),('Cheddar Cheese','2024-04-17'),('Chicken','2024-04-17'),('Dough','2024-04-17'),('garlic','2024-04-18'),('Mozzarella Cheese','2024-04-17'),('olive oil','2024-04-18'),('Parmesan Cheese','2024-04-17'),('Pasta','2024-04-17'),('Pizza Sauce','2024-04-17'),('Spaghetti','2024-04-17');
/*!40000 ALTER TABLE `Ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Instruction`
--

DROP TABLE IF EXISTS `Instruction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Instruction` (
  `recipe_title` varchar(50) NOT NULL,
  `cook_time` varchar(50) DEFAULT NULL,
  `prep_time` varchar(50) DEFAULT NULL,
  `servings` int DEFAULT NULL,
  `calories` int DEFAULT NULL,
  PRIMARY KEY (`recipe_title`),
  CONSTRAINT `instruction_ibfk_1` FOREIGN KEY (`recipe_title`) REFERENCES `Recipe` (`title`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Instruction`
--

LOCK TABLES `Instruction` WRITE;
/*!40000 ALTER TABLE `Instruction` DISABLE KEYS */;
INSERT INTO `Instruction` VALUES ('Chicken Parm','20 mins','15 mins',3,1000),('Mac','12 min','5 min',5,1500),('Pizza','25 mins','10',3,1000);
/*!40000 ALTER TABLE `Instruction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rating`
--

DROP TABLE IF EXISTS `Rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rating` (
  `recipe_title` varchar(50) DEFAULT NULL,
  `score` int DEFAULT NULL,
  `description` text,
  `date_added` date DEFAULT NULL,
  KEY `recipe_title` (`recipe_title`),
  CONSTRAINT `rating_ibfk_1` FOREIGN KEY (`recipe_title`) REFERENCES `Recipe` (`title`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rating`
--

LOCK TABLES `Rating` WRITE;
/*!40000 ALTER TABLE `Rating` DISABLE KEYS */;
INSERT INTO `Rating` VALUES ('Chicken Parm',5,'Best meal','2024-04-16'),('Pizza',3,'Bad for me','2024-04-17'),('Mac',5,'Greater recipe!','2024-04-17');
/*!40000 ALTER TABLE `Rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Recipe`
--

DROP TABLE IF EXISTS `Recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Recipe` (
  `title` varchar(50) NOT NULL,
  `description` text,
  `date_published` date DEFAULT NULL,
  PRIMARY KEY (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Recipe`
--

LOCK TABLES `Recipe` WRITE;
/*!40000 ALTER TABLE `Recipe` DISABLE KEYS */;
INSERT INTO `Recipe` VALUES ('Chicken Parm','So good!','2024-04-16'),('Mac','Cheesier and delicious!','2024-04-17'),('Pizza','Cheat Meal','2024-04-17');
/*!40000 ALTER TABLE `Recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RecipeList`
--

DROP TABLE IF EXISTS `RecipeList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RecipeList` (
  `name` varchar(50) NOT NULL,
  `description` text,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RecipeList`
--

LOCK TABLES `RecipeList` WRITE;
/*!40000 ALTER TABLE `RecipeList` DISABLE KEYS */;
INSERT INTO `RecipeList` VALUES ('Pastas','For the italians'),('Uno','Healthy foods!');
/*!40000 ALTER TABLE `RecipeList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RincludesI`
--

DROP TABLE IF EXISTS `RincludesI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RincludesI` (
  `recipe_title` varchar(50) DEFAULT NULL,
  `ingredient_name` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  KEY `recipe_title` (`recipe_title`),
  KEY `ingredient_name` (`ingredient_name`),
  CONSTRAINT `rincludesi_ibfk_1` FOREIGN KEY (`recipe_title`) REFERENCES `Recipe` (`title`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `rincludesi_ibfk_2` FOREIGN KEY (`ingredient_name`) REFERENCES `Ingredient` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RincludesI`
--

LOCK TABLES `RincludesI` WRITE;
/*!40000 ALTER TABLE `RincludesI` DISABLE KEYS */;
INSERT INTO `RincludesI` VALUES ('Chicken Parm','Chicken','2 Breasts'),('Chicken Parm','Parmesan Cheese','0.5 lbs'),('Pizza','Dough','1 Bag'),('Pizza','Pizza Sauce','1 Jar'),('Pizza','Mozzarella Cheese','1 lb'),('Mac','Spaghetti','Half a package'),('Mac','Parmesan Cheese','1 cup'),('Mac','Black Pepper','1 teaspoon');
/*!40000 ALTER TABLE `RincludesI` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RinRL`
--

DROP TABLE IF EXISTS `RinRL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RinRL` (
  `recipe_title` varchar(50) DEFAULT NULL,
  `recipe_list_name` varchar(50) DEFAULT NULL,
  KEY `recipe_title` (`recipe_title`),
  KEY `recipe_list_name` (`recipe_list_name`),
  CONSTRAINT `rinrl_ibfk_1` FOREIGN KEY (`recipe_title`) REFERENCES `Recipe` (`title`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `rinrl_ibfk_2` FOREIGN KEY (`recipe_list_name`) REFERENCES `RecipeList` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RinRL`
--

LOCK TABLES `RinRL` WRITE;
/*!40000 ALTER TABLE `RinRL` DISABLE KEYS */;
INSERT INTO `RinRL` VALUES ('Chicken Parm','Uno'),('Mac','Pastas');
/*!40000 ALTER TABLE `RinRL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Steps`
--

DROP TABLE IF EXISTS `Steps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Steps` (
  `recipe_title` varchar(50) DEFAULT NULL,
  `id` int DEFAULT NULL,
  `description` text,
  KEY `recipe_title` (`recipe_title`),
  CONSTRAINT `steps_ibfk_1` FOREIGN KEY (`recipe_title`) REFERENCES `Recipe` (`title`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Steps`
--

LOCK TABLES `Steps` WRITE;
/*!40000 ALTER TABLE `Steps` DISABLE KEYS */;
INSERT INTO `Steps` VALUES ('Chicken Parm',1,'Cook chicken'),('Chicken Parm',2,'Cook sauce'),('Chicken Parm',3,'Melt cheese on top'),('Pizza',1,'Spread dough'),('Pizza',2,'Add toppings'),('Pizza',3,'Put in oven'),('Mac',1,'Bring water to boil.'),('Mac',2,'Add pasta.');
/*!40000 ALTER TABLE `Steps` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-18  0:10:10
