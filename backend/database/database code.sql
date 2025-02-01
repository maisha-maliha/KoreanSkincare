CREATE DATABASE KoreanSkinCare;
USE KoreanSkinCare;
CREATE TABLE userInfo (
	user_id INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(255),
    full_name VARCHAR(255),
    user_email VARCHAR(255),
    user_password VARCHAR(255),
    PRIMARY KEY (user_id)
);

CREATE TABLE productsInfo (
	product_id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(255),
    product_details TEXT,
	product_quantity INT,
    product_sold INT,
    brand_name VARCHAR(255),
    PRIMARY KEY (product_id)
);

INSERT INTO userInfo(user_name, full_name, user_email, user_password) VALUES 
("maisha", "maliha tabassum", "maisha@gmail.com", "maisha"),
("maliha", "maisha anika", "anika@gmail.com", "maisha22"),
("maisha", "maliha tabassum", "maliha@gmail.com", "maisha44 ");

INSERT INTO productsInfo(product_name, product_details, product_quantity, product_sold, brand_name) VALUES
("Skin 1004 centeall toning toner", "its an amazing toner with light exfoliation. its has PHA,", 5,3,"Skin1004"),
("Skin 1004 tone brightening toner", "its an amazing toner that contains derivation vitamin c,", 15,8,"Skin1004");

SELECT * FROM userInfo;
SELECT * FROM productsInfo;



