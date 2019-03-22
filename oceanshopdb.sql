-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2019 年 03 月 21 日 09:36
-- 伺服器版本: 10.1.35-MariaDB
-- PHP 版本： 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `oceanshopdb`
--

-- --------------------------------------------------------

--
-- 資料表結構 `admin`
--

CREATE TABLE `admin` (
  `adid` int(11) NOT NULL,
  `adname` varchar(50) NOT NULL,
  `ademail` varchar(100) NOT NULL,
  `adpw` varchar(1000) NOT NULL,
  `adtype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `admin`
--

INSERT INTO `admin` (`adid`, `adname`, `ademail`, `adpw`, `adtype`) VALUES
(1, 'Wong Tie Man', 'qaz@qaz', 'qaz', 'owner'),
(2, 'Chan jon sa', 'wsx@wsx', 'wsx', 'developer');

-- --------------------------------------------------------

--
-- 資料表結構 `comments`
--

CREATE TABLE `comments` (
  `cid` int(11) NOT NULL,
  `proid` int(11) NOT NULL,
  `userID` int(11) DEFAULT NULL,
  `ctime` datetime NOT NULL,
  `comment` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `comments`
--

INSERT INTO `comments` (`cid`, `proid`, `userID`, `ctime`, `comment`) VALUES
(1, 1, 11, '2019-03-16 08:25:13', 'qwertyu, i am a test comment.'),
(2, 15, 11, '2019-03-16 12:41:34', 'nice game ! recommand !'),
(4, 15, 6, '2019-03-16 12:47:08', '+1 , the most awesome Open-World mode'),
(6, 15, 12, '2019-03-16 12:52:31', 'yeayrayaasdasdasjkhgdjkashvfgcxjakhgsfdujkavhsyxgcjaygvfsdjkaGFSXZckujahgsfvdkuzYgf'),
(7, 15, 12, '2019-03-16 13:00:58', 'kisfydgkiSfegkuiSYGfdkuiSYfdkguySGFDffffffffffffffffslkdfygKUSFYDGkuSfydgikuSfydgokUSIfydgukSfydgkusfydgkuSfydgkuSfdgkuSdgfkuSdgfkuSYGdfkusgkuSfydgkuSYGfdkuSfdgkuSydgfkuSfydgkSUDfygkSUfydgkUSFDG'),
(8, 15, 1, '2019-03-16 15:57:38', 'oh yeah , buy it with discount XDDDD'),
(9, 34, 14, '2019-03-17 15:17:23', 'this is a rubbish game , if u wanna play with cheater , go and buy , otherwise u will be  regret !!!');

-- --------------------------------------------------------

--
-- 資料表結構 `orders`
--

CREATE TABLE `orders` (
  `orderID` int(11) NOT NULL,
  `uuid` int(11) NOT NULL,
  `ppid` int(11) NOT NULL,
  `truename` varchar(50) NOT NULL,
  `howmany` int(11) NOT NULL,
  `place` text NOT NULL,
  `mobilen` int(11) NOT NULL,
  `buydate` datetime NOT NULL,
  `arrdate` date NOT NULL,
  `sopition` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `orders`
--

INSERT INTO `orders` (`orderID`, `uuid`, `ppid`, `truename`, `howmany`, `place`, `mobilen`, `buydate`, `arrdate`, `sopition`) VALUES
(8, 12, 3, 'penny', 1, 'dfg', 345, '2019-03-15 16:15:32', '2019-03-20', 'none'),
(9, 12, 2, 'qwer', 1, 'dfg', 345, '2019-03-15 16:15:53', '2019-03-20', 'none'),
(10, 12, 8, 'wwewr', 1, 'dfg', 345, '2019-03-15 16:21:37', '2019-03-20', 'none'),
(11, 12, 13, 'diu', 1, 'dfg', 345, '2019-03-15 16:24:06', '2019-03-20', 'none'),
(12, 12, 33, 'tyutyud', 1, 'dfg', 345, '2019-03-15 16:24:36', '2019-03-20', 'none'),
(13, 12, 18, 'uiop', 1, 'dfg', 345, '2019-03-15 16:26:50', '2019-03-20', 'none'),
(14, 12, 28, 'iojpguio', 1, 'dfg', 345, '2019-03-15 16:27:03', '2019-03-20', 'none'),
(15, 1, 3, 'qwe', 1, 'qwe', 123, '2019-03-15 16:51:13', '2019-03-20', 'none');

-- --------------------------------------------------------

--
-- 資料表結構 `products`
--

CREATE TABLE `products` (
  `pID` int(11) NOT NULL,
  `pname` varchar(50) NOT NULL,
  `pprice` float NOT NULL,
  `description` text NOT NULL,
  `quantity` int(11) NOT NULL,
  `category` varchar(30) NOT NULL,
  `plink` text NOT NULL,
  `date` datetime NOT NULL,
  `uploader` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `products`
--

INSERT INTO `products` (`pID`, `pname`, `pprice`, `description`, `quantity`, `category`, `plink`, `date`, `uploader`) VALUES
(1, 'Simple White Color T-Shirt ', 20, 'Simple White Color T-Shirt , 100% make by cotton. Make in China.', 100, 'tshirt', 'ts1.jpg', '2019-03-13 20:23:03', '1'),
(2, 'Simple Black Color T-Shirt', 20, 'Simple Black Color T-Shirt, 100% make by cotton , make in China .', 50, 'tshirt', 'ts2.jpg', '2019-03-13 20:24:14', '1'),
(3, 'ME ME BIG BOY T-SHIRT', 50, 'This premium short sleeve shirt is made with 4.2-ounce, 100% ring spun combed cotton for the ultimate in soft feel, weight, and durability.\r\nHeather colors are made of a super soft cotton/poly blend.\r\nAvailable in S through 2XL sizes.', 50, 'tshirt', 'ts3.jpg', '2019-03-13 22:07:05', '1'),
(4, 'Montane Dart T-Shirt', 45, 'Breathable\r\nWicking\r\nPOLYGIENE® permanent odour control\r\nFlatlocked sewn seams', 50, 'tshirt', 'ts4.jpg', '2019-03-15 16:18:40', '1'),
(5, 'TieLabs Black T-shirt', 40, 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo', 50, 'tshirt', 'ts5.jpg', '2019-03-16 19:51:05', '1'),
(6, 'Blue Jeans “Chula” Wms', 120, 'Made in Portugal\r\n,97% CO, 3% EA\r\n,5 Pockets\r\n,Slim Fit\r\n,strech\r\n,Colour: Denim Blue', 20, 'jeans', 'jn1.jpg', '2019-03-13 02:08:05', '6'),
(7, 'MUSTANG STONEWASH JEAN', 221, 'Mustang Stretch Jean\r\n,Short leg\r\n,Close fit\r\n,Low rise\r\n,Straight leg\r\n,Standard jean pockets\r\n,Machine wash\r\n,98% Cotton, 2% Elastane\r\n,Sizes are given as the waist measurement in centimetres', 30, 'jeans', 'jn2.jpg', '2019-03-13 07:35:49', '6'),
(8, 'Shrink to Fit Jeans Rigid Indigo', 280, '100% Cotton ,14 oz DenimMid Rise , Original Classic FitButton Fly , Straight Leg17\" Leg Opening, Quintessential Anti-FitContrast Stitching.', 410, 'jeans', 'jn3.jpg', '2019-03-13 16:06:51', '6'),
(9, 'Aura 311 Bootcut Jeans', 298, '100% cotton , made in hong kong', 40, 'jeans', 'jn4.jpg', '2019-03-14 07:15:38', '6'),
(10, 'SLIM PALAZZO FLARE JEANS', 528, 'Hovering somewhere between your best-loved boyfriend jeans and great wide-leg trousers, these fantastic-fitting jeans—check out the sexy high waist—are the ones you’ll reach for on the weekends (with a tee and sneakers), weeknights (add a silky blouse and spiky heels), and at work (add a button-up and mules). We’re big fans of the deep indigo wash and light fading through the legs.', 50, 'jeans', 'jn5.jpg', '2019-03-13 13:13:46', '6'),
(11, 'Tailored Jeans', 80, 'Super slim and comfy lorem ipsum lorem jeansum. Lorem jeamsun denim lorem jeansum.', 40, 'jeans', 'jn6.jpg', '2019-03-12 08:09:38', '11'),
(12, 'F1 2018', 258, 'MAKE HEADLINES in F1® 2018. F1® 2018 is the official videogame of the 2018 FIA FORMULA ONE WORLD CHAMPIONSHIP™. Become immersed in the world of Formula 1® more than ever before.Build your reputation both on and off the track, with time-pressured media interviews that influence your F1 career path.', 999, 'games', 'gm1.png', '2019-03-14 05:41:39', '11'),
(13, 'Pixel Game Maker MV ', 368, 'Game Jam Submissions\r\nFor the Remix Game Jam, assets from the sample games already available in Pixel Game Maker MV must be used to create a new “remixed” project.', 999, 'games', 'gm2.png', '2019-03-14 05:12:43', '11'),
(14, 'Middle-earth Shadow of War', 299, 'Experience an epic open-world brought to life by the award-winning Nemesis System. Forge a new Ring of Power, conquer Fortresses in massive battles and dominate Mordor with your personal orc army in Middle-earth™: Shadow of War™.', 999, 'games', 'gm3.png', '2019-03-14 07:21:18', '11'),
(15, 'Grand Theft Auto V', 125, 'Los Santos is a city of bright lights, long nights and dirty secrets, and they don’t come brighter, longer or dirtier than in GTA Online: After Hours. The party starts now.', 999, 'games', 'gm4.jpg', '2019-03-14 05:29:12', '11'),
(16, 'Tom Clancy\'s Rainbow Six® Siege', 109, 'Tom Clancy\'s Rainbow Six Siege is the latest installment of the acclaimed first-person shooter franchise developed by the renowned Ubisoft Montreal studio.', 999, 'games', 'gm5.jpg', '2019-03-14 12:08:45', '6'),
(17, 'Iphone 8 Plus', 5000, 'Available space is less and varies due to many factors. A standard configuration uses approximately 10GB to 12GB of space (including iOS and preinstalled apps) depending on the model and settings. Preinstalled apps use about 4GB, and you can delete these apps and restore them.', 200, 'mobile', 'iphone8.jpg', '2019-03-14 03:11:30', '1'),
(18, 'Iphone XR', 8500, 'Available space is less and varies due to many factors. A standard configuration uses approximately 10GB to 12GB of space (including iOS and preinstalled apps) depending on the model and settings. Preinstalled apps use about 4GB, and you can delete these apps and restore them.', 200, 'mobile', 'iphonexr.png', '2019-03-14 00:06:14', '1'),
(19, 'BlackBerry Key2', 6000, 'BlackBerry® KEY2 Specifications\r\n100% Android™\r\nAccess to over a million apps on Google Play\r\nFirst dual main camera BlackBerry smartphone\r\nAll new reimagined keyboard design\r\nUp to 2 days battery life', 50, 'mobile', 'bb1.png', '2019-03-14 03:27:00', '1'),
(20, 'SamSung S10', 10000, 'After being available for pre-order since February 21, the Samsung Galaxy S10, S10+, and S10e are now all out of the pre-order stage and available for immediate purchase.\r\n\r\nAs we expected, this means that the previous pre-order bonus of getting a $130 gift certificate with your order is gone. In its place, Samsung is now offering 6 months of Spotify Premium for free.', 500, 'mobile', 's10.jpg', '2019-03-16 06:27:13', '6'),
(21, 'MIA Single Upholstered Bed', 4590.95, 'This designer Mia single upholstered bed is available in both a Natural Linen Look & Pink Velvet Fabric. This quality bed will enhance any bedroom.\r\n\r\nThe craftsmanship of this bed is superb, design is very current and price is a fraction of what you would pay for a similar bed from chain bedding stores\r\n\r\nWith no sharp corners or edges, this bed is sure to impress! Included: 1 x headboard, 1 x footboard, 1 x set of side rails, 1 x set of timber base slats\r\n\r\nNot Included: Mattress, Pillows, Sheets, child safety rail Features', 50, 'home', 'bed1.jpg', '2019-03-14 19:23:39', '6'),
(22, 'ihome Saver Bed & Pull Out', 15499, 'Imported Fabric Bed Made From Malaysia,\r\n,Bed frameLVL Wood Frame w/ 2 Center ,Support and Legs\r\n,LVL mean Lamintaed Veneer Lumber is high ,strength engineered wood product used ,primarily for structural application\r\n,King Size 72\"x78\" with 36\"x75\" Pull Out,\r\nQueenSize 60\"x75\" with 36\"x75\" Pull Out ,\r\nDouble Size 54\"x75\" with 36\"x75\" Pull Out', 65, 'home', 'bed2.jpg', '2019-03-14 12:12:32', '6'),
(23, 'Abbotson Linen Bed Cover', 253, 'Pillowcases and accessories sold separately.\r\nFront & Reverse: 100% Linen – Quilted, Each quilted square is 9.95cm x 9.95cm\r\nFilling: 95% Cotton, 5% Polyester\r\nLining: 100% Polypropylene\r\nProduct Code: S28P\r\nDesigned in : Australia\r\nMade in : China', 88, 'home', 'bed3.jpg', '2019-03-14 06:03:02', '11'),
(24, 'CUSTOM CLOSETS & CLOSET', 35000, 'The professional designer assigned for your custom closet will review your organization needs, provide you with custom designs based off of the scope of your project and take measurements.', 999, 'home', 'closet1.jpg', '2019-03-14 00:00:44', '11'),
(25, 'Build Your Own Melamine Closet ', 32599, 'Walk through the closet aisle at any home center and you\'ll see lots of closet organizers-everything from wire shelving systems to ones that look like real wood cabinetry with all kinds of fancy accessories. And while these systems are designed to work in just about any type of closet, you can get a fully custom white closet organizer (and possibly even save a few bucks)by building one yourself. Here\'s how we built ours using melamine panels, plus some tips on building your own.', 999, 'home', 'closet2.jpg', '2019-03-14 23:00:00', '11'),
(26, 'Sherlock Ext. Dining Table & 4 Chairs', 2400, 'An elegantly carved pedestal base supports the extending table top, the underside painted with a subtle grey for a beautiful finish. A traditional wooden table top maintains the classic aesthetic this piece aims for, its versatile design allowing it to be extended from 1.1m – 1.5 m which is perfect for unexpected guests or hosting parties.', 60, 'home', 'table1.jpg', '2019-03-14 09:13:43', '1'),
(27, 'SIENA Dinning Table', 16000, 'Siena is the definitive example of Alf\'s ability to combine classical and contemporary, with a high-gloss black finish and sharp design lines. The table can extended from a 6 seater to an 8 seater.', 20, 'home', 'table2.jpg', '2019-03-14 02:16:59', '6'),
(28, 'ELEGANT TV STAND FOR TV\'S UP TO 75\" WITH STORAGE', 1699.99, 'This contemporary and elegant Techni Mobili TV stand, for TVs up to 75\", is designed to fit any bedroom or family room. It includes three drawers and 3 shelves providing storage for your electronics and gaming accessories. Middle shelf has a back panel opening for cable management. The Techni Mobili TV cabinet is made of heavy duty compressed wood and laminate surface that is resistant to scratches. Important: Holds TV\'s up to 75\" when TV is measure diagonally. Actual unit is 71\" wide but TV overhang on either side is suitable. Color: Hickory & Walnut', 20, 'home', 'tvstand1.jpg', '2019-03-14 01:06:10', '11'),
(29, 'Dakota 60\" TV Stand', 2789.9, 'This gorgeous TV console will be a perfect fit in your living room! Featuring four cabinets for storing your television and audio electronics, this console is finished in a beautiful espresso. The melamine coating means this console is difficult to scratch and easy to clean, while the medium density fibreboard construction means this console is strong and durable!\r\n\r\nDimensions\r\nWidth: 60.04\" (152.5 cm)Height: 24.02\" (61.0 cm)Depth: 15.43\" (39.2 cm)', 20, 'home', 'tvstand2.jpg', '2019-03-14 19:49:43', '11'),
(31, 'Apex Legends', 10, 'Choose from a lineup of outlaws, soldiers, misfits, and misanthropes, each with their own set of skills. The Apex Games welcome all comers – survive long enough, and they call you a Legend.', 999, 'games', 'apex.jpg', '2019-03-14 19:16:47', '12'),
(32, 'Iphone XS', 12000, '512 gb version . Super Retina in two sizes — including the largest display ever on an iPhone. Even faster Face ID. The smartest, most powerful chip in a smartphone. And a breakthrough dual-camera system with Depth Control. iPhone XS is everything you love about iPhone. Taken to the extreme.', 20, 'mobile', 'iphonexs.jpg', '2019-03-14 20:12:32', '12'),
(34, 'PLAYERUNKNOWN\'S BATTLEGROUNDS', 160, 'PLAYERUNKNOWN\'S BATTLEGROUNDS is a battle royale shooter that pits 100 players against each other in a struggle for survival. Gather supplies and outwit your opponents to become the last person standing.', 60, 'games', 'pubg.jpg', '2019-03-15 19:58:45', '12');

-- --------------------------------------------------------

--
-- 資料表結構 `users`
--

CREATE TABLE `users` (
  `userID` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `useremail` varchar(100) NOT NULL,
  `userpw` varchar(1000) NOT NULL,
  `usermobile` int(11) NOT NULL,
  `useraddress` varchar(100) NOT NULL,
  `registerdate` date NOT NULL,
  `profilepicture` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `users`
--

INSERT INTO `users` (`userID`, `username`, `useremail`, `userpw`, `usermobile`, `useraddress`, `registerdate`, `profilepicture`) VALUES
(1, 'qwe', 'qwe@qwe', '$2b$12$UPWw3NQ9b1ml5dXlrZjo/uYVdpQ8N/n8Hqxpr1zHsSzGgbDrdcsHm', 123123123, 'password:qwe', '2019-03-12', '/avatars/nopic.png'),
(6, 'poi', 'poi@poi', '$2b$12$WTeHS0MleXE0Z5r4v6.sm.1nOOHrORYT.YH7qdGyFSrWdFEVUyt7q', 234, 'poi', '2019-03-12', '/avatars/nopic.png'),
(11, 'asd', 'asd@asd', '$2b$12$ClBRiSulAXpln0LOlfM4AOoIWPsxckyvmtykSq3j/IiohpqM7/47e', 98, 'qweasd', '2019-03-13', '/avatars/nopic.png'),
(12, 'dfg', 'dfg@dfg', '$2b$12$20i8ErhDOJt7.m3sdiwVQ.f1S9nob40P/d1X2IjmmdB8Q3oO7KFpK', 345, 'dfg', '2019-03-14', '/avatars/nopic.png'),
(13, 'qqq', 'qqq@qqq', '$2b$12$VUiRJhM./cIJW8uxUfIJYO35eLwGqrsS8GC0dq56qJceJwFIbW7S6', 12333, 'qqq', '2019-03-14', '/avatars/nopic.png'),
(14, 'ggg', 'ggg@ggg', '$2b$12$8Ag3ThJ12ziCpVPr5VYs/.iwFAMfNM7TRvKiI86RH3YM.rfjRfJbu', 666, 'ggg', '2019-03-17', '/avatars/nopic.png');

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`adid`);

--
-- 資料表索引 `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`cid`),
  ADD KEY `userID` (`userID`);

--
-- 資料表索引 `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`orderID`);

--
-- 資料表索引 `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`pID`);

--
-- 資料表索引 `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userID`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `admin`
--
ALTER TABLE `admin`
  MODIFY `adid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用資料表 AUTO_INCREMENT `comments`
--
ALTER TABLE `comments`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- 使用資料表 AUTO_INCREMENT `orders`
--
ALTER TABLE `orders`
  MODIFY `orderID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- 使用資料表 AUTO_INCREMENT `products`
--
ALTER TABLE `products`
  MODIFY `pID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- 使用資料表 AUTO_INCREMENT `users`
--
ALTER TABLE `users`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- 已匯出資料表的限制(Constraint)
--

--
-- 資料表的 Constraints `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
