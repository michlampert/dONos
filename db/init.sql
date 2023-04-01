CREATE TABLE Company (
    CompanyID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255)
);

CREATE TABLE Employee (
    EmployeeID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255)
);

CREATE TABLE Leaderboard (
    LeaderboardID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Score INT,
    CompanyID INT NOT NULL,
    EmployeeID INT NOT NULL,

    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE Donos (
    Content TEXT,
    Donor INT NOT NULL,
    Reciver INT NOT NULL,
    LeaderboardID INT NOT NULL,

    FOREIGN KEY (Donor) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (Reciver) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (LeaderboardID) REFERENCES Leaderboard(LeaderboardID)
);
