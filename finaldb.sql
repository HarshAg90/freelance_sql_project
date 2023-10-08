/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - 142ngo
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`142ngo` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `142ngo`;

/*Table structure for table `admindetails` */

DROP TABLE IF EXISTS `admindetails`;

CREATE TABLE `admindetails` (
  `uid` int(255) NOT NULL auto_increment,
  `uname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL default '',
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  PRIMARY KEY  (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `admindetails` */

insert  into `admindetails`(`uid`,`uname`,`lname`,`email`,`password`,`phone`) values (1,'s','a','s@gmail.com','s','976767997'),(2,'admin','admin','admin@gmail.com','1234','8693815309');

/*Table structure for table `basicinfo` */

DROP TABLE IF EXISTS `basicinfo`;

CREATE TABLE `basicinfo` (
  `Bid` int(255) NOT NULL auto_increment,
  `uname` varchar(255) default NULL,
  `lname` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `phone` varchar(255) default NULL,
  `dob` varchar(255) default NULL,
  `gender` varchar(255) default NULL,
  `city` varchar(255) default NULL,
  `state` varchar(255) default NULL,
  `aboutme` longtext,
  `studyat` varchar(255) default NULL,
  `studyfrom` varchar(255) default NULL,
  `studyto` varchar(255) default NULL,
  `verifytag` varchar(2000) default NULL,
  PRIMARY KEY  (`Bid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `basicinfo` */

insert  into `basicinfo`(`Bid`,`uname`,`lname`,`email`,`phone`,`dob`,`gender`,`city`,`state`,`aboutme`,`studyat`,`studyfrom`,`studyto`,`verifytag`) values (1,'rakesh','xyz','r@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(2,'siddhesh','shinde','s@gmail.com','9658741230',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(3,'Siddhesh','Shinde','siddheshsureshshinde@gmail.com','9324133767',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(4,'Suraj','Tetme','tetmesuraj@gmail.com','8693815309',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(5,'Yogesh ','Pendse','yogpendse2000@gmail.com','8793453667',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(6,'Keval','Shetta','kevalshetta@gmail.com','8693815309',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(7,'Apurva','Gadkari','apurvagadkari@gmail.com','8693815309',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(8,'Sofia','Shaikh','sofiashaikh1998@gmail.com','8693815309',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(9,'user','test','testuser@gmail.com','8693815309',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(10,'ngo','ngos','ngo@gmail.com','8693815309',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(11,'example','example','tetmesuraj@gmail.com','8879005756',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png');

/*Table structure for table `basicinfo1` */

DROP TABLE IF EXISTS `basicinfo1`;

CREATE TABLE `basicinfo1` (
  `Basicid` int(255) NOT NULL auto_increment,
  `uname` varchar(255) default NULL,
  `lname` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `phone` varchar(255) default NULL,
  `dob` varchar(255) default NULL,
  `gender` varchar(255) default NULL,
  `city` varchar(255) default NULL,
  `state` varchar(255) default NULL,
  `aboutme` longtext,
  `studyat` varchar(255) default NULL,
  `studyfrom` varchar(255) default NULL,
  `studyto` varchar(255) default NULL,
  `verifytag` varchar(2000) default NULL,
  PRIMARY KEY  (`Basicid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `basicinfo1` */

insert  into `basicinfo1`(`Basicid`,`uname`,`lname`,`email`,`phone`,`dob`,`gender`,`city`,`state`,`aboutme`,`studyat`,`studyfrom`,`studyto`,`verifytag`) values (1,'rakesh','xyz','r@gmail.com','654120389',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/verify.png'),(2,'siddhesh','shinde','s@gmail.com','9658741230',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/verify.png'),(3,'Siddhesh','Shinde','siddheshsureshshinde@gmail.com','9324133767',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/verify.png'),(4,'Suraj','Tetme','tetmesuraj@gmail.com','8693815309',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/verify.png'),(5,'Yogesh','Pendse','yogpendse2000@gmail.com','8793453667',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/verify.png'),(6,'Keval','Shetta	','kevalshetta@gmail.com','8693815309	',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(7,'Apurva	','Gadkari','apurvagadkari@gmail.com	','8693815309',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(8,'Sofia','Shaikh','sofiashaikh1998@gmail.com	','8693815309',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/verify.png'),(9,'user','test','testuser@gmail.com	','8693815309',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(10,'example','example','tetmesuraj@gmail.com	','8879005756	',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png'),(11,'ngo	','ngos','ngo@gmail.com	','8693815309',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'../static/images/unverify.png');

/*Table structure for table `certificate` */

DROP TABLE IF EXISTS `certificate`;

CREATE TABLE `certificate` (
  `Cid` int(255) NOT NULL auto_increment,
  `uname` varchar(255) NOT NULL,
  `certifyImg` varchar(255) NOT NULL,
  PRIMARY KEY  (`Cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `certificate` */

insert  into `certificate`(`Cid`,`uname`,`certifyImg`) values (1,'Apurva','OIP_2.jpg'),(2,'Suraj','certificate.jpg');

/*Table structure for table `followunfollow` */

DROP TABLE IF EXISTS `followunfollow`;

CREATE TABLE `followunfollow` (
  `Fid` int(255) NOT NULL auto_increment,
  `user1` varchar(255) NOT NULL,
  `user2` varchar(255) NOT NULL,
  `follow` varchar(255) default '',
  `unfollow` varchar(255) default '',
  PRIMARY KEY  (`Fid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `followunfollow` */

insert  into `followunfollow`(`Fid`,`user1`,`user2`,`follow`,`unfollow`) values (16,'siddhesh','Yogesh','1',''),(17,'siddhesh','Apurva','1',''),(18,'siddhesh','rakesh','1',''),(19,'Suraj','siddhesh','1',''),(21,'Suraj','Sofia','1',''),(22,'Suraj','example','1','');

/*Table structure for table `like_comnt` */

DROP TABLE IF EXISTS `like_comnt`;

CREATE TABLE `like_comnt` (
  `id` int(255) NOT NULL auto_increment,
  `pid` varchar(255) NOT NULL,
  `uname` varchar(255) NOT NULL,
  `tags` varchar(255) NOT NULL,
  `likes` varchar(255) default NULL,
  `comments` longtext,
  `dislikes` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `like_comnt` */

/*Table structure for table `notifyuser` */

DROP TABLE IF EXISTS `notifyuser`;

CREATE TABLE `notifyuser` (
  `Nid` int(255) NOT NULL auto_increment,
  `uname` varchar(255) NOT NULL,
  `notify` longtext NOT NULL,
  PRIMARY KEY  (`Nid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notifyuser` */

insert  into `notifyuser`(`Nid`,`uname`,`notify`) values (1,'rakesh','siddhesh Started following you!'),(2,'rakesh','siddhesh Started Unfollow you!'),(3,'siddhesh','siddhesh Give like to your Environment post'),(4,'rakesh','Siddhesh Started following you!'),(5,'rakesh','Siddhesh Started Unfollow you!'),(6,'Siddhesh','Siddhesh Give like to your Environment post'),(7,'Siddhesh','Siddhesh Give like to your Environment post'),(8,'Siddhesh','Siddhesh Give like to your Environment post'),(9,'rakesh','Siddhesh Started following you!'),(10,'Suraj','Sofia Started following you!'),(11,'Keval','Suraj Started following you!'),(12,'Suraj','Suraj Give like to your childcare post'),(13,'Suraj','Suraj Give like to your childcare post'),(14,'Suraj','Suraj Give like to your childcare post'),(15,'Suraj','Suraj Give like to your Environment post'),(16,'Suraj','Suraj Give like to your Environment post'),(17,'Suraj','Suraj Give like to your Environment post'),(18,'Suraj','Suraj Give like to your Environment post'),(19,'Suraj','Suraj Give like to your childcare post'),(20,'Suraj','Suraj Give like to your childcare post'),(21,'Suraj','Suraj Give like to your childcare post'),(22,'Sofia','Sofia Give like to your Environment post'),(23,'Sofia','Sofia Give like to your Environment post'),(24,'Sofia','Sofia Give like to your Environment post'),(25,'Sofia','Sofia Give like to your Environment post'),(26,'Sofia','Sofia Give like to your Environment post'),(27,'Sofia','Sofia Give like to your Environment post'),(28,'Sofia','Sofia Give like to your Environment post'),(29,'Sofia','Sofia Give like to your Environment post'),(30,'siddhesh','Apurva Started following you!'),(31,'Sofia','Apurva Started following you!'),(32,'Yogesh','Suraj Started following you!'),(33,'rakesh','siddhesh Started Unfollow you!'),(34,'Apurva','siddhesh Started following you!'),(35,'user','siddhesh Started following you!'),(36,'rakesh','siddhesh Started following you!'),(37,'example','siddhesh Started following you!'),(38,'ngo','siddhesh Started following you!'),(39,'siddhesh','siddhesh Give like to your Environment post'),(40,'Suraj','Sofia Started Unfollow you!'),(41,'Sofia','Sofia Give like to your childcare post'),(42,'Sofia','Sofia Give like to your childcare post'),(43,'Sofia','Sofia Give like to your childcare post'),(44,'Sofia','Sofia Give like to your childcare post'),(45,'Sofia','Sofia Give like to your childcare post'),(46,'Sofia','Sofia Give like to your childcare post'),(47,'Sofia','Sofia Give like to your childcare post'),(48,'Sofia','Sofia Give like to your childcare post'),(49,'Sofia','Sofia Give like to your childcare post'),(50,'Sofia','Sofia Give like to your childcare post'),(51,'Sofia','Sofia Give like to your Environment post'),(52,'Sofia','Sofia Give like to your Environment post'),(53,'Sofia','Sofia Give like to your Environment post'),(54,'Sofia','Sofia Give like to your Environment post'),(55,'rakesh','siddhesh Started following you!'),(56,'Keval','siddhesh Started following you!'),(57,'rakesh','siddhesh Started Unfollow you!'),(58,'Yogesh','siddhesh Started following you!'),(59,'Keval','siddhesh Started Unfollow you!'),(60,'Sofia','Sofia Give like to your childcare post'),(61,'Sofia','Sofia Give like to your childcare post'),(62,'Sofia','Sofia Give like to your Environment post'),(63,'Apurva','Apurva Give like to your Environment post'),(64,'Apurva','Apurva Give like to your Environment post'),(65,'Apurva','Apurva Give like to your Environment post'),(66,'Apurva','Apurva Give like to your childcare post'),(67,'siddhesh','siddhesh Give like to your childcare post'),(68,'siddhesh','siddhesh Give like to your childcare post'),(69,'user','user Give like to your Environment post'),(70,'user','user Give like to your childcare post'),(71,'user','user Give like to your Environment post'),(72,'siddhesh','siddhesh Give like to your childcare post'),(73,'siddhesh','siddhesh Give like to your childcare post'),(74,'siddhesh','siddhesh Give like to your childcare post'),(75,'Apurva','siddhesh Started following you!'),(76,'rakesh','siddhesh Started following you!'),(77,'siddhesh','siddhesh Give like to your childcare post'),(78,'siddhesh','siddhesh Give like to your childcare post'),(79,'siddhesh','siddhesh Give like to your Environment post'),(80,'siddhesh','siddhesh Give like to your Environment post'),(81,'siddhesh','siddhesh Give like to your Environment post'),(82,'siddhesh','siddhesh Give like to your Environment post'),(83,'siddhesh','siddhesh Give like to your Environment post'),(84,'siddhesh','Suraj Started following you!'),(85,'user','Suraj Started following you!'),(86,'user','Suraj Started Unfollow you!'),(87,'Sofia','Suraj Started following you!'),(88,'example','Suraj Started following you!'),(89,'siddhesh','siddhesh Give like to your Environment post'),(90,'rakesh','rakesh Give like to your Environment post'),(91,'rakesh','rakesh Give like to your Environment post'),(92,'rakesh','rakesh Give like to your childcare post'),(93,'rakesh','rakesh Give like to your Environment post'),(94,'rakesh','rakesh Give like to your Environment post'),(95,'rakesh','rakesh Give like to your Environment post'),(96,'ngo','ngo Give like to your Environment post'),(97,'ngo','ngo Give like to your childcare post');

/*Table structure for table `post_comment` */

DROP TABLE IF EXISTS `post_comment`;

CREATE TABLE `post_comment` (
  `id` int(255) NOT NULL auto_increment,
  `pid` varchar(255) default NULL,
  `uname` varchar(255) default NULL,
  `posttag` varchar(255) default NULL,
  `cmnt` longtext,
  `pstime` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `post_comment` */

insert  into `post_comment`(`id`,`pid`,`uname`,`posttag`,`cmnt`,`pstime`) values (1,'1','rakesh','Environment','nice post','2022-05-05'),(2,'4','Sofia','childcare','Niceeee','2022-05-05'),(3,'2','Siddhesh','childcare','Niceeee','2022-05-07');

/*Table structure for table `recomended_posts` */

DROP TABLE IF EXISTS `recomended_posts`;

CREATE TABLE `recomended_posts` (
  `Psid` int(255) NOT NULL auto_increment,
  `uname` varchar(255) default NULL,
  `postid` varchar(255) default NULL,
  PRIMARY KEY  (`Psid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `recomended_posts` */

insert  into `recomended_posts`(`Psid`,`uname`,`postid`) values (3,'rakesh','7'),(4,'rakesh','8'),(5,'rakesh','9'),(6,'ngo','1'),(7,'ngo','6'),(8,'ngo','7'),(9,'ngo','8'),(10,'ngo','9'),(11,'ngo','4'),(12,'ngo','5'),(13,'ngo','11');

/*Table structure for table `recomnd` */

DROP TABLE IF EXISTS `recomnd`;

CREATE TABLE `recomnd` (
  `id` int(255) NOT NULL auto_increment,
  `uid` varchar(255) NOT NULL,
  `pid` varchar(255) NOT NULL,
  `likes` varchar(255) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `recomnd` */

insert  into `recomnd`(`id`,`uid`,`pid`,`likes`) values (1,'7','1','6'),(2,'7','11','7'),(3,'2','12','4'),(4,'2','2','8'),(5,'9','3','3'),(6,'9','5','9'),(7,'9','4','1'),(8,'2','7','2'),(9,'2','6','8'),(10,'2','8','3'),(11,'2','9','4'),(12,'2','10','8'),(13,'2','13','8'),(17,'2','1','7'),(18,'2','1','8'),(19,'1','1','9'),(20,'1','2','9'),(21,'1','3','4'),(22,'1','1','10'),(23,'1','2','10'),(24,'1','2','2'),(25,'10','2','3'),(26,'10','3','5');

/*Table structure for table `unfollowing` */

DROP TABLE IF EXISTS `unfollowing`;

CREATE TABLE `unfollowing` (
  `Ufid` int(255) NOT NULL auto_increment,
  `user1` varchar(255) default NULL,
  `user2` varchar(255) default NULL,
  `unfollow` varchar(255) default NULL,
  PRIMARY KEY  (`Ufid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `unfollowing` */

/*Table structure for table `userdetails` */

DROP TABLE IF EXISTS `userdetails`;

CREATE TABLE `userdetails` (
  `uid` int(255) NOT NULL auto_increment,
  `uname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL default '',
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `field_interest` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  `follow` varchar(255) NOT NULL,
  `unfollow` varchar(255) NOT NULL,
  `verifytag` longtext NOT NULL,
  PRIMARY KEY  (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `userdetails` */

insert  into `userdetails`(`uid`,`uname`,`lname`,`email`,`password`,`phone`,`field_interest`,`role`,`follow`,`unfollow`,`verifytag`) values (1,'rakesh','xyz','a@gmail.com','a','28487248929','environment','Ngo','2','3','../static/images/unverify.png'),(2,'siddhesh','shinde','s@gmail.com','sid','9658741230','[\'education\']','volunteer','2','0','../static/images/unverify.png'),(3,'Siddhesh','Shinde','siddheshsureshshinde@gmail.com','1234','9324133767','[\'education\', \'environment\', \'animals\']','volunteer','2','0','../static/images/unverify.png'),(4,'Suraj','Tetme','tetmesuraj@gmail.com','1234','8693815309','[\'environment\', \'animals\']','volunteer','0','2','../static/images/unverify.png'),(5,'Yogesh ','Pendse','yogpendse2000@gmail.com','1234','8793453667','[\'environment\', \'animals\']','volunteer','2','0','../static/images/unverify.png'),(6,'Keval','Shetta','kevalshetta@gmail.com','1234','8693815309','[\'education\', \'environment\']','volunteer','1','3','../static/images/unverify.png'),(7,'Apurva','Gadkari','apurvagadkari@gmail.com','1234','8693815309','[\'animals\']','volunteer','2','0','../static/images/unverify.png'),(8,'Sofia','Shaikh','sofiashaikh1998@gmail.com','1234','8693815309','[\'animals\']','volunteer','2','0','../static/images/unverify.png'),(9,'user','test','testuser@gmail.com','1234','8693815309','[\'environment\']','volunteer','1','3','../static/images/unverify.png'),(10,'ngo','ngos','ngo@gmail.com','1234','8693815309','[\'animals\']','Ngo','1','0','../static/images/unverify.png'),(11,'example','example','tetmesuraj@gmail.com','1234','8879005756','[\'environment\']','volunteer','2','0','../static/images/unverify.png');

/*Table structure for table `userpost` */

DROP TABLE IF EXISTS `userpost`;

CREATE TABLE `userpost` (
  `pid` int(255) NOT NULL auto_increment,
  `uname` varchar(255) NOT NULL default '',
  `caption` longtext,
  `post_img` varchar(255) default '',
  `tag` varchar(255) default '',
  `post_dt` varchar(255) NOT NULL,
  `likes` varchar(255) default NULL,
  `comments` longtext,
  `dislike` varchar(255) default NULL,
  PRIMARY KEY  (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `userpost` */

insert  into `userpost`(`pid`,`uname`,`caption`,`post_img`,`tag`,`post_dt`,`likes`,`comments`,`dislike`) values (1,'rakesh','hello environment','download.jpg','Environment','2022-05-05','10',NULL,NULL),(2,'siddhesh','Greenpeace India.\r\nThis is one of the best Indian Environmental NGOs, and whose reach extends to over 55 other countries globally. It ','OIP_3.jpg','Environment','2022-05-07','3',NULL,NULL),(3,'siddhesh','Smile Foundation.\r\nOne of the most prominent NGOs in India, Child-line focuses on child safety and protection through a 24 hours helpline with exceptional turn-around time. C','R_1.jpg','childcare','2022-05-07','5',NULL,NULL),(4,'siddhesh','Child-Line India\r\nThis NGO has been doing exceptional work for the past 13 years providing healthcare and education for underprivileged children.','Help_for_Poor_Child-_amiga_ngo.JPG','childcare','2022-05-07','1',NULL,NULL),(5,'Suraj','Help Delhi Breathe .This is a non-profit environmental organization that was formed in 2015 to help bring to an end, the air pollution crisis in Delhi, India.','Na','Environment','2022-05-07','9',NULL,NULL),(6,'Suraj','Help Delhi Breathe .This is a non-profit environmental organization that was formed in 2015 to help bring to an end, the air pollution crisis in Delhi, India.','saveenvironment.jpg','Environment','2022-05-07','8',NULL,NULL),(7,'Suraj','CRY.\r\nCRY or â€˜Child Rights and Youâ€™ focuses on child education, healthcare, nutrition and special learning needs.','b93577c2b7b626db54b9ae0cdd87c202.jpg','childcare','2022-05-07','2',NULL,NULL),(8,'Apurva','Samveda offers special treatment and training facilities for mentally challenged students, dyslexic children and kids with fine motor disabilities. ','28102016045204284ingoodcompany-768x481.jpg','childcare','2022-05-07','3',NULL,NULL),(9,'Apurva','This is a branch of Clean Air Asia, which also has other offices in the Philippines and China. The organization has had its presence in India for over a decade now (since 2008).','Na','Environment','2022-05-07','4',NULL,NULL),(10,'Apurva','This is a branch of Clean Air Asia, which also has other offices in the Philippines and China. The organization has had its presence in India for over a decade now (since 2008).','swachh-bharat2.jpg','Environment','2022-05-07','8',NULL,NULL),(11,'Sofia','Established back in 1994, the Wildlife Protection Society of India (WPSI) works to bring a fresh focus, in tackling the overwhelming Indian wildlife crisis. ','33.jpg','Environment','2022-05-08','7',NULL,NULL),(12,'Sofia','Child health','blogger-image-184957325.jpg','childcare','2022-05-08','4',NULL,NULL),(13,'Sofia','One of the oldest NGOs to help children in the country, Pratham has been working with children of Mumbai slums for the past 20 years.','R_2.jpg','Environment','2022-05-08','8',NULL,NULL),(22,'Suraj','Paani Foundation.','pani.jpg','Environment','2022-05-08',NULL,NULL,NULL),(23,'Keval','\r\nThe Akshaya Patra Foundation is a not-for-profit organisation headquartered in Bengaluru, India.','food.jpg','childcare','2022-05-08',NULL,NULL,NULL),(24,'Keval','ENGO â€“ An environmental NGO like Greenpeace.','env.jpg','Environment','2022-05-08',NULL,NULL,NULL),(25,'Keval','Child Rights and You .Save the Children has a robust presence in as many as 16 states of India. Our projects and interventions are designed to better the lives of underprivileged children ','edu.jpg','childcare','2022-05-08',NULL,NULL,NULL),(26,'Suraj','WILDLIFE CONSERVATION SOCIETY\r\n','people-for-animals-cropped-1588235946.jpg','Environment','2022-05-08',NULL,NULL,NULL),(27,'Suraj','Forests, Climate and Biomass Working Group, Environmental Paper Network Environmental Paper Network (EPN) is a global coalition of over 150 NGOs working together','forest.jpg','Environment','2022-05-08',NULL,NULL,NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
