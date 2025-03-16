-- CREATE DATABASE
CREATE DATABASE KoreanSkinCare;
USE KoreanSkinCare;

-- PRODUCT TABEL
CREATE TABLE Products(
	productId INT NOT NULL AUTO_INCREMENT,
    productName VARCHAR(100),
    brandId INT,
    price INT,
    discount INT,
    visibility INT,
PRIMARY KEY (productId)
);

-- BRAND TABLE
CREATE TABLE brands(
	brandId INT AUTO_INCREMENT NOT NULL,
    brandName VARCHAR(80),
    country VARCHAR(50),
    visibility INT,
    PRIMARY KEY (brandId)
);

-- PRODUCT TYPE TABLE
CREATE TABLE productType(
	typeId INT NOT NULL AUTO_INCREMENT,
    typeName VARCHAR(30),
    PRIMARY KEY (typeId)
);

-- INGREDIENTS TABLE
CREATE TABLE ingredients(
	ingredientId INT NOT NULL AUTO_INCREMENT,
    ingredientName VARCHAR(50),
    PRIMARY KEY (ingredientId)
);

-- SKIN TYPE TABLE
CREATE TABLE skin(
	skinId INT NOT NULL AUTO_INCREMENT,
    skinName VARCHAR(50),
    PRIMARY KEY (skinId)
);

-- SKIN CONCERN TABLE
CREATE TABLE concerns(
	concernId INT NOT NULL AUTO_INCREMENT,
    concern VARCHAR(20),
    PRIMARY KEY (concernId)
);

-- REVIEW TABLE
CREATE TABLE reviews(
	reviewId INT NOT NULL AUTO_INCREMENT,
	userId INT,
	productId INT,
	reviewDate DATETIME,
	rating INT,
	reviewDetails VARCHAR(255),
    PRIMARY KEY (reviewId)
);

-- USERS TABLE
CREATE TABLE users(
	userId INT NOT NULL AUTO_INCREMENT,
    createdTime DATETIME,
    userName VARCHAR(50),
    address VARCHAR(120),
    email VARCHAR(50),
    phone VARCHAR(20),
    age DATE,
    userPassword VARCHAR(120),
    PRIMARY KEY (userId)
);

-- CREATE INVENTORY TABLE
CREATE TABLE inventory(
	inventoryId INT NOT NULL AUTO_INCREMENT,
    productId INT,
    quantity INT,
    PRIMARY KEY (inventoryId)
);

-- ADMIN TABLE
CREATE TABLE admins(
	adminId INT NOT NULL AUTO_INCREMENT,
    adminName VARCHAR(50),
    email VARCHAR(50),
    adminPassword VARCHAR(120),
    adminRole VARCHAR(30),
    PRIMARY KEY (adminId)
);

CREATE TABLE orders(
	orderId INT NOT NULL AUTO_INCREMENT,
    userId INT,
    orderDate DATETIME,
    deliveryDate DATETIME,
    discount INT, -- if discount on whole order
    totalPaid INT,
    address VARCHAR(120),
    paymentMethod INT,
    PRIMARY KEY (orderId)
);

CREATE TABLE soldProducts(
	orderId INT,
    productId INT,
    quantity INT,
    perCost INT,
    perDiscount INT, -- discount on per product
    totalCost INT
);

CREATE TABLE paymentmethods(
	methodId INT NOT NULL AUTO_INCREMENT,
    methodName VARCHAR(50),
    PRIMARY KEY (methodId)
);