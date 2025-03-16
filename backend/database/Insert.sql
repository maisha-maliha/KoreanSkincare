USE KoreanSkinCare;

INSERT INTO admins (adminName, email, adminPassword, adminRole) VALUES
('Admin One', 'admin1@example.com', 'hashed_admin_password_1', 'Manager'),
('Admin Two', 'admin2@example.com', 'hashed_admin_password_2', 'Moderator');

INSERT INTO users (createdTime, userName, address, email, phone, age, userPassword) VALUES
(NOW(), 'Alice Kim', 'Seoul, South Korea', 'alice@example.com', '821012345678', '1995-06-15', 'hashed_password_1'),
(NOW(), 'John Park', 'Busan, South Korea', 'john@example.com', '821098765432', '1992-09-20', 'hashed_password_2'),
(NOW(), 'Emma Lee', 'Incheon, South Korea', 'emma@example.com', '821076543210', '1998-03-05', 'hashed_password_3');


INSERT INTO brands (brandName, country, visibility) VALUES
('Beauty of Joseon', 'South Korea', 1),
('Numbuzin', 'South Korea', 1),
('Klairs', 'South Korea', 1),
('COSRX', 'South Korea', 1),
('Some By Mi', 'South Korea', 1),
('Isntree', 'South Korea', 1);

INSERT INTO Products (productName, brandId, price, discount, visibility) VALUES
-- Beauty of Joseon
('Glow Serum: Propolis + Niacinamide', 1, 18, 10, 1),
('Relief Sun: Rice + Probiotics SPF50+', 1, 20, 5, 1),
('Dynasty Cream', 1, 25, 0, 1),

-- Numbuzin
('No.3 Skin Softening Serum', 2, 22, 8, 1),
('No.5 Vitamin Concentrated Serum', 2, 24, 12, 1),
('No.3 Super Glowing Essence Toner', 2, 21, 7, 1),

-- Klairs
('Supple Preparation Facial Toner', 3, 21, 5, 1),
('Freshly Juiced Vitamin Drop', 3, 23, 10, 1),
('Midnight Blue Calming Cream', 3, 27, 0, 1),

-- COSRX
('Pure Fit Cica Cleansing Oil', 4, 25, 5, 1),
('Low pH Good Morning Gel Cleanser', 4, 12, 10, 1),
('One Step Original Clear Pad', 4, 22, 8, 1),

-- Some By Mi
('Bye Bye Blackhead 30 Days Miracle Green Tea Tox', 5, 24, 7, 1),
('AHA BHA PHA 30 Days Miracle Acne Clear Foam', 5, 15, 10, 1),
('AHA BHA PHA 30 Days Miracle Toner Pad', 5, 23, 5, 1),

-- Isntree
('Mugwort Calming Cleansing Oil', 6, 28, 5, 1),
('Green Tea Fresh Cleanser', 6, 18, 8, 1),
('Chestnut BHA 2% Clear Toner Pad', 6, 20, 6, 1);

INSERT INTO productType (typeName) VALUES
('Serum'),
('Sunscreen'),
('Moisturizer'),
('Cleansing Oil'),
('Foam Cleanser'),
('Toner Pad');

INSERT INTO skin (skinName) VALUES
('Oily'),
('Dry'),
('Combination'),
('Sensitive'),
('Normal');

INSERT INTO concerns (concern)
VALUES 
    ('Acne'),
    ('Wrinkles'),
    ('Dryness'),
    ('Oily skin'),
    ('Redness'),
    ('Hyperpigmentation'),
    ('Eczema'),
    ('Psoriasis'),
    ('Dark circles'),
    ('Rosacea'),
    ('Sunburn'),
    ('Sensitivity');


INSERT INTO ingredients (ingredientName) VALUES
('Niacinamide'),
('Hyaluronic Acid'),
('Centella Asiatica'),
('Green Tea'),
('Propolis'),
('Vitamin C'),
('AHA'),
('BHA'),
('PHA'),
('Rice Extract');

INSERT INTO inventory (productId, quantity) VALUES
(1, 100),
(2, 150),
(3, 200),
(4, 120),
(5, 180),
(6, 90),
(7, 160),
(8, 130),
(9, 110),
(10, 170),
(11, 140),
(12, 100);

INSERT INTO paymentmethods (methodName) VALUES
('Credit Card'),
('PayPal'),
('Bkash'),
('Bank Transfer'),
('Cash on Delivery');

INSERT INTO orders (userId, orderDate, deliveryDate, discount, totalPaid, address, paymentMethod) VALUES
(1, NOW(), DATE_ADD(NOW(), INTERVAL 3 DAY), 5, 45, 'Seoul, South Korea', 1),
(2, NOW(), DATE_ADD(NOW(), INTERVAL 5 DAY), 10, 60, 'Busan, South Korea', 2),
(3, NOW(), DATE_ADD(NOW(), INTERVAL 2 DAY), 0, 30, 'Incheon, South Korea', 3);

INSERT INTO soldProducts (orderId, productId, quantity, perCost, perDiscount, totalCost) VALUES
(1, 1, 2, 18, 10, 36),
(1, 2, 1, 20, 5, 19),
(2, 3, 1, 25, 0, 25),
(2, 4, 1, 25, 5, 24),
(3, 5, 2, 12, 10, 22),
(3, 6, 1, 22, 8, 20);

INSERT INTO reviews (userId, productId, reviewDate, rating, reviewDetails) VALUES
(1, 1, NOW(), 5, 'Great serum, very hydrating!'),
(2, 2, NOW(), 4, 'Good sunscreen, lightweight and no white cast.'),
(3, 3, NOW(), 5, 'Perfect moisturizer for my skin!'),
(1, 4, NOW(), 4, 'Oil cleanser removes makeup well.'),
(2, 5, NOW(), 5, 'The cleanser is gentle and doesn’t strip the skin.'),
(3, 6, NOW(), 4, 'Toner pads are very refreshing.');


SELECT * FROM brands;
SELECT * FROM products;
SELECT * FROM productType;
SELECT * FROM ingredients;
SELECT * FROM skin;
SELECT * FROM concerns;
SELECT * FROM reviews;
SELECT * FROM users;
SELECT * FROM inventory;
SELECT * FROM admins;
SELECT * FROM orders;
SELECT * FROM soldProducts;
SELECT * FROM paymentmethods;
SELECT 
products.productId, 
products.productName, 
brands.brandName, 
products.price, 
products.discount, 
products.visibility as productVisibility
FROM products 
INNER JOIN brands ON products.brandId = brands.brandId 
WHERE brands.visibility = 1;


-- ALTER TABLE users DROP COLUMN phone;
-- ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- UPDATE users
-- SET userPassword = '$2b$12$8VxhoFvzmNiqWiktpBbpP.52t4lsoz5Ehnei/HIz6sfBcYUnCxone'
-- WHERE userId = 2;  -- Specify the admin's ID or any other criteria to identify the admin

-- DELETE FROM admins
-- WHERE adminId = 4;  -- Replace 1 with the actual adminId you want to delete


