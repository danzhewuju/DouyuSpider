# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.21)
# Database: douyu
# Generation Time: 2018-12-04 12:30:07 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table host_info
# ------------------------------------------------------------

DROP TABLE IF EXISTS `host_info`;

CREATE TABLE `host_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id序号',
  `room_number` char(50) NOT NULL COMMENT '直播间号',
  `username` char(200) NOT NULL COMMENT '主播名称',
  `kind` char(200) NOT NULL COMMENT '主播类型',
  `online` int(11) DEFAULT NULL,
  `w_number` int(11) DEFAULT NULL COMMENT '观看人数',
  `coefficient` float DEFAULT NULL COMMENT '影响因数',
  `link` char(200) DEFAULT NULL COMMENT '直播间链接',
  `timestamp` timestamp NULL DEFAULT NULL COMMENT '爬取时间',
  `followers` int(11) DEFAULT NULL COMMENT '关注人数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
