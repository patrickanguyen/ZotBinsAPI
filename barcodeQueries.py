insert_query = "INSERT INTO `Barcodes` (`name`, `type`, `barcode`, `wasteBin`, `instructions`) VALUES (%s,%s, %s, %s, %s);"
get_query = "SELECT * FROM `Barcodes` WHERE `barcode` = %s;"