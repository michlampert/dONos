CREATE TABLE Company (
    CompanyID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255)
);

CREATE TABLE Employee (
    EmployeeID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255),
    CompanyID INT NOT NULL,

    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);

CREATE TABLE Donos (
    Content TEXT,
    Donor INT NOT NULL,
    Receiver INT NOT NULL,
    Status ENUM('waiting', 'rejected', 'accepted') NOT NULL,
    Score INT,

    FOREIGN KEY (Donor) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (Receiver) REFERENCES Employee(EmployeeID)
);
