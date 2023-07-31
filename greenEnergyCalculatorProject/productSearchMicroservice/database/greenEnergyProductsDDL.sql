-- Table creation

CREATE OR REPLACE TABLE `GreenEnergyProducts` (
    productID int NOT NULL,
    genericName varchar(250),
    greenEnergyType varchar(50),
    cost decimal(10, 2),
    power decimal(10, 0),
    description varchar(250),
    PRIMARY KEY (productID)
);


-- Some values that will be inserted

INSERT INTO `GreenEnergyProducts` (productID, genericName, greenEnergyType, cost, power, description)
VALUES 
('1', 'REC Solar N-PEAK 3 Black Series 400 Watt Monocrystalline Solar Module', 'solar', 340, 400, 'Nominal power: 400 Watts, Number of cells: 132 half-cut, Power tolerance: 0 / +5 Watts, Vmp: 37.6 Volts, Voc: 45.0 Volts, Imp: 10.64 Amps, Isc: 11.39 Amps, Module efficiency: 20.3%, Dimensions (inches): 74.8 x 40.9 x 1.2, Weight: 48.0 lbs'),
('2', 'Missouri Freedom 48 Volt 2000 Watt Wind Turbine and VRD Classic MPPT Kit', 'wind', 4144.49, 2000, '48 Volt 2000 Watt Freedom Wind Turbine featuring three Missouri Falcon blades, 100 Feet 12/6 SJOO Cable, All in One Pre-Wired Missouri VRD Midnite Classic Charge Controller Board');