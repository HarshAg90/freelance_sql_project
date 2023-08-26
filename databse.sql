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

insert  into `post_comment`(`id`,`pid`,`uname`,`posttag`,`cmnt`,`pstime`) values (1,'3','aniket','Environment','â€œAway, away, from men and towns,\r\nTo the wild wood and the downs, â€”\r\nTo the silent wilderness,\r\nWhere the soul need not repress its music.â€\r\nâ€”Percy Bysshe Shelley','2022-04-24');

/*Table structure for table `userdetails` */

DROP TABLE IF EXISTS `userdetails`;

CREATE TABLE `userdetails` (
  `uid` int(255) NOT NULL auto_increment,
  `uname` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `field_interest` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  PRIMARY KEY  (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `userdetails` */

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

insert  into `userpost`(`pid`,`uname`,`caption`,`post_img`,`tag`,`post_dt`,`likes`,`comments`,`dislike`) values (1,'aniket','abc xyz asd','Na','childcare','2022-04-24','2',NULL,'3'),(3,'aniket','â€œI only feel angry when I see waste. When I see people throwing away things we could use.â€\r\nâ€”Mother Teresa','Mother-Teresa-Shared-400x600.jpg','Environment','2022-04-24','2','  Away, away, from men and towns,\r\nTo the wild wood and the downs, â€”\r\nTo the silent wilderness,\r\nWhere the soul need not repress its music.|','2');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
