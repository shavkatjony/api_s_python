SELECT 
    c.CustomerName, 
    o.OrderID, 
    p.ProductName
FROM Customers c
LEFT JOIN (Orders o 
    INNER JOIN Products p ON o.ProductID = p.ProductID) 
ON c.CustomerID = o.CustomerID;
