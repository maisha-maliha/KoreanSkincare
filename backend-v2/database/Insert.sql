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

INSERT INTO Products (productName, details, brandId, price, discount, visibility) VALUES
-- Beauty of Joseon
('Glow Serum: Propolis + Niacinamide', 'A lightweight serum infused with propolis and niacinamide to brighten and hydrate skin.', 1, 18, 10, 1),
('Relief Sun: Rice + Probiotics SPF50+', 'A lightweight, non-greasy sunscreen with rice extract and probiotics for UV protection and hydration.', 1, 20, 5, 1),
('Dynasty Cream', 'A rich yet non-greasy moisturizer with rice bran water and ginseng extract for deep hydration.', 1, 25, 0, 1),

-- Numbuzin
('No.3 Skin Softening Serum', 'A nourishing serum that improves skin texture and hydration with niacinamide and fermented ingredients.', 2, 22, 8, 1),
('No.5 Vitamin Concentrated Serum', 'A brightening serum packed with vitamins to enhance radiance and even out skin tone.', 2, 24, 12, 1),
('No.3 Super Glowing Essence Toner', 'A hydrating toner with fermented extracts and panthenol to boost skin’s glow.', 2, 21, 7, 1),

-- Klairs
('Supple Preparation Facial Toner', 'A gentle hydrating toner with amino acids that soothe and balance the skin.', 3, 21, 5, 1),
('Freshly Juiced Vitamin Drop', 'A vitamin C serum designed to brighten skin and reduce the appearance of dark spots.', 3, 23, 10, 1),
('Midnight Blue Calming Cream', 'A soothing cream with centella asiatica and guaiazulene for calming sensitive skin.', 3, 27, 0, 1),

-- COSRX
('Pure Fit Cica Cleansing Oil', 'A gentle cleansing oil with cica extract to remove makeup and impurities without irritation.', 4, 25, 5, 1),
('Low pH Good Morning Gel Cleanser', 'A mild gel cleanser with tea tree oil and BHA for gentle exfoliation and fresh skin.', 4, 12, 10, 1),
('One Step Original Clear Pad', 'Exfoliating toner pads infused with betaine salicylate to unclog pores and prevent breakouts.', 4, 22, 8, 1),

-- Some By Mi
('Bye Bye Blackhead 30 Days Miracle Green Tea Tox', 'A gentle foaming cleanser with green tea and BHA to remove blackheads and impurities.', 5, 24, 7, 1),
('AHA BHA PHA 30 Days Miracle Acne Clear Foam', 'A multi-acid cleanser that exfoliates and soothes acne-prone skin.', 5, 15, 10, 1),
('AHA BHA PHA 30 Days Miracle Toner Pad', 'Pre-soaked toner pads with AHA, BHA, and PHA for gentle exfoliation and acne care.', 5, 23, 5, 1),

-- Isntree
('Mugwort Calming Cleansing Oil', 'A soothing cleansing oil with mugwort extract to remove impurities while calming sensitive skin.', 6, 28, 5, 1),
('Green Tea Fresh Cleanser', 'A refreshing gel cleanser with green tea extract that controls excess oil and soothes skin.', 6, 18, 8, 1),
('Chestnut BHA 2% Clear Toner Pad', 'Toner pads infused with chestnut shell extract and BHA for gentle exfoliation and clear skin.', 6, 20, 6, 1);


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

INSERT INTO productIngredients (productId, ingredientId) VALUES
-- Beauty of Joseon
(1, 5),  -- Propolis
(1, 1),  -- Niacinamide
(2, 10), -- Rice Extract
(3, 2),  -- Hyaluronic Acid

-- Numbuzin
(4, 1),  -- Niacinamide
(4, 2),  -- Hyaluronic Acid
(5, 6),  -- Vitamin C
(6, 2),  -- Hyaluronic Acid

-- Klairs
(7, 2),  -- Hyaluronic Acid
(8, 6),  -- Vitamin C
(9, 3),  -- Centella Asiatica

-- COSRX
(10, 3), -- Centella Asiatica
(11, 7), -- AHA
(11, 8), -- BHA
(12, 8), -- BHA

-- Some By Mi
(13, 4), -- Green Tea
(14, 7), -- AHA
(14, 8), -- BHA
(14, 9), -- PHA
(15, 9), -- PHA

-- Isntree
(16, 3), -- Centella Asiatica
(17, 4), -- Green Tea
(18, 8); -- BHA

INSERT INTO productSkin (productId, skintId) VALUES
-- Beauty of Joseon
(1, 3), -- Combination
(1, 5), -- Normal
(2, 2), -- Dry
(3, 4), -- Sensitive

-- Numbuzin
(4, 3), -- Combination
(4, 5), -- Normal
(5, 2), -- Dry
(6, 4), -- Sensitive

-- Klairs
(7, 1), -- Oily
(7, 3), -- Combination
(8, 5), -- Normal
(9, 4), -- Sensitive

-- COSRX
(10, 4), -- Sensitive
(11, 1), -- Oily
(12, 1), -- Oily
(12, 3), -- Combination

-- Some By Mi
(13, 1), -- Oily
(13, 3), -- Combination
(14, 1), -- Oily
(14, 3), -- Combination
(15, 4), -- Sensitive

-- Isntree
(16, 4), -- Sensitive
(17, 1), -- Oily
(17, 3), -- Combination
(18, 1); -- Oily;

INSERT INTO productConcerns (productId, concernId) VALUES
-- Beauty of Joseon
(1, 6),  -- Hyperpigmentation
(2, 11), -- Sunburn
(3, 3),  -- Dryness

-- Numbuzin
(4, 6),  -- Hyperpigmentation
(5, 2),  -- Wrinkles
(6, 3),  -- Dryness

-- Klairs
(7, 3),  -- Dryness
(8, 6),  -- Hyperpigmentation
(9, 5),  -- Redness

-- COSRX
(10, 5), -- Redness
(11, 1), -- Acne
(12, 1), -- Acne

-- Some By Mi
(13, 1), -- Acne
(14, 1), -- Acne
(15, 1), -- Acne

-- Isntree
(16, 5), -- Redness
(17, 1), -- Acne
(18, 1); -- Acne

INSERT INTO productProductType (productId, productTypetId) VALUES
-- Beauty of Joseon
(1, 1), -- Glow Serum -> Serum
(2, 2), -- Relief Sun -> Sunscreen
(3, 3), -- Dynasty Cream -> Moisturizer

-- Numbuzin
(4, 1), -- No.3 Skin Softening Serum -> Serum
(5, 1), -- No.5 Vitamin Concentrated Serum -> Serum
(6, 6), -- No.3 Super Glowing Essence Toner -> Toner Pad

-- Klairs
(7, 6), -- Supple Preparation Facial Toner -> Toner Pad
(8, 1), -- Freshly Juiced Vitamin Drop -> Serum
(9, 3), -- Midnight Blue Calming Cream -> Moisturizer

-- COSRX
(10, 4), -- Pure Fit Cica Cleansing Oil -> Cleansing Oil
(11, 5), -- Low pH Good Morning Gel Cleanser -> Foam Cleanser
(12, 6), -- One Step Original Clear Pad -> Toner Pad

-- Some By Mi
(13, 4), -- Bye Bye Blackhead Green Tea Tox -> Cleansing Oil
(14, 5), -- AHA BHA PHA Miracle Acne Clear Foam -> Foam Cleanser
(15, 6), -- AHA BHA PHA Miracle Toner Pad -> Toner Pad

-- Isntree
(16, 4), -- Mugwort Calming Cleansing Oil -> Cleansing Oil
(17, 5), -- Green Tea Fresh Cleanser -> Foam Cleanser
(18, 6); -- Chestnut BHA 2% Clear Toner Pad -> Toner Pad



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

SELECT * FROM products WHERE productId IN (1,14,15,16);


-- ALTER TABLE users DROP COLUMN phone;
-- ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- UPDATE users
-- SET userPassword = '$2b$12$8VxhoFvzmNiqWiktpBbpP.52t4lsoz5Ehnei/HIz6sfBcYUnCxone'
-- WHERE userId = 2;  -- Specify the admin's ID or any other criteria to identify the admin

-- DELETE FROM admins
-- WHERE adminId = 4;  -- Replace 1 with the actual adminId you want to delete


