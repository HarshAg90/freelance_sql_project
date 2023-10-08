/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - socailawareness
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`socailawareness` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `socailawareness`;

/*Table structure for table `comments` */

DROP TABLE IF EXISTS `comments`;

CREATE TABLE `comments` (
  `id` int(255) NOT NULL auto_increment,
  `uname` varchar(255) default NULL,
  `lname` varchar(255) default NULL,
  `idofpost` varchar(255) default NULL,
  `timestamp` varchar(255) default NULL,
  `comment` longtext,
  `commenter` varchar(255) default NULL,
  `time` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `comments` */

insert  into `comments`(`id`,`uname`,`lname`,`idofpost`,`timestamp`,`comment`,`commenter`,`time`) values (1,'Amol','Nerlekar','1','22-08-2023 10:56','Mast video ahe hi !','mayurkatkar','22-08-2023 11:54');

/*Table structure for table `extrainfo` */

DROP TABLE IF EXISTS `extrainfo`;

CREATE TABLE `extrainfo` (
  `username` varchar(255) default NULL,
  `address` longtext,
  `city` varchar(255) default NULL,
  `maritalstatus` varchar(255) default NULL,
  `Qualification` varchar(255) default NULL,
  `age` varchar(255) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `extrainfo` */

insert  into `extrainfo`(`username`,`address`,`city`,`maritalstatus`,`Qualification`,`age`) values ('mayurkatkar','vedika soc sagar nagar vikhroli park site','Mumbai','Married','MSC.CS','34');

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

insert  into `followunfollow`(`Fid`,`user1`,`user2`,`follow`,`unfollow`) values (1,'a','b','1',''),(2,'mayurkatkar','b','1',''),(3,'mayurkatkar','a','1',''),(4,'b','mayurkatkar','1','');

/*Table structure for table `notifyuser` */

DROP TABLE IF EXISTS `notifyuser`;

CREATE TABLE `notifyuser` (
  `Nid` int(255) NOT NULL auto_increment,
  `uname` varchar(255) NOT NULL,
  `notify` longtext NOT NULL,
  PRIMARY KEY  (`Nid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notifyuser` */

insert  into `notifyuser`(`Nid`,`uname`,`notify`) values (1,'b','a Started following you!'),(2,'b','mayurkatkar Started following you!'),(3,'a','mayurkatkar Started following you!'),(4,'b','mayurkatkar commented on your post.'),(5,'b','mayurkatkar liked on your post.'),(6,'mayurkatkar','b Started following you!');

/*Table structure for table `posts` */

DROP TABLE IF EXISTS `posts`;

CREATE TABLE `posts` (
  `id` int(255) NOT NULL auto_increment,
  `uploader` varchar(255) default NULL,
  `postimage` varchar(255) default NULL,
  `posttext` longtext,
  `timestamp` varchar(255) default NULL,
  `likecount` int(255) default '0',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `posts` */

insert  into `posts`(`id`,`uploader`,`postimage`,`posttext`,`timestamp`,`likecount`) values (1,'b','static/posts/b/slider-image-1.jpg','The items are packed flush to each other toward the right edge of the alignment container in the appropriate axis. If the property\'s axis is not parallel with the inline axis (in a grid container) or the main-axis (in a flexbox container), this value behaves like','22-08-2023 10:56',1),(2,'mayurkatkar','static/posts/mayurkatkar/property2.jpg','Nice house !','22-08-2023 11:52',0);

/*Table structure for table `poststoadmin` */

DROP TABLE IF EXISTS `poststoadmin`;

CREATE TABLE `poststoadmin` (
  `id` int(255) NOT NULL auto_increment,
  `uploader` varchar(255) default NULL,
  `postimage` varchar(255) default NULL,
  `posttext` longtext,
  `timestamp` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `poststoadmin` */

/*Table structure for table `userdetails` */

DROP TABLE IF EXISTS `userdetails`;

CREATE TABLE `userdetails` (
  `uid` int(255) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `uname` varchar(255) default NULL,
  `lname` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `password` varchar(255) default NULL,
  `phone` varchar(255) default NULL,
  `dob` varchar(255) default NULL,
  `profilepic` varchar(255) default 'static/images/profilepic.png',
  `follow` int(255) default '0',
  `unfollow` int(255) default '0',
  PRIMARY KEY  (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `userdetails` */

insert  into `userdetails`(`uid`,`username`,`uname`,`lname`,`email`,`password`,`phone`,`dob`,`profilepic`,`follow`,`unfollow`) values (1,'a','Yash','Salvi','yashsalvi1999@gmail.com','a','9930090883','2023-08-24','static/posts/a/slider-image-2.jpg',6,2),(2,'b','Amol','Nerlekar','amolnerlekar@gmail.com','b','8548586596','2023-08-24','static/images/profilepic.png',11,4),(4,'c','Roshan','Mundekar','roshan12@gmail.com','c','344234234234','2023-08-23','static/posts/a/property4.jpg',3,5),(5,'d','Sushant','Tawar','stawar@gmail.com','d','565656565656','2023-08-22','static/posts/d/slider-image-4.jpg',3,2),(6,'jay','Jay','Salvi','jay@gmail.com','j','5478596585','2023-08-15','static/posts/jay/property2.jpg',0,0),(7,'mayurkatkar','Mayur','Katkar','katkarM@gmail.com','mayur','8545854548','2023-08-19','static/posts/mayurkatkar/slider-image-2.jpg',1,0);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
