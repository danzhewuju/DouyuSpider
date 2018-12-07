host_infoCREATE DATABASE douyu;
use douyu;

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