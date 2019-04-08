-- -----------
-- Table structure for 'course3'
-- -----------
DROP TABLE IF EXISTS `course3`;
CREATE TABLE `course3` (
  `id` int NOT NULL,
  `sub1` varchar(20), 
  `sub2` varchar(20),
  `sub3` varchar(20),
  `amount` int,
  PRIMARY KEY(`id`)
)DEFAULT CHARSET=utf8 COMMENT='七选三课程人数分布';

