/*
  Warnings:

  - You are about to drop the `Book` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropTable
DROP TABLE "Book";

-- CreateTable
CREATE TABLE "User" (
    "id" SERIAL NOT NULL,
    "email" TEXT NOT NULL,
    "systemId" INTEGER NOT NULL,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "System" (
    "id" SERIAL NOT NULL,
    "nominalVoltageOfElement" DOUBLE PRECISION NOT NULL,
    "capacityOfOneElement" DOUBLE PRECISION NOT NULL,
    "series" INTEGER NOT NULL,
    "paralel" INTEGER NOT NULL,
    "numberOfBatteryPacks" INTEGER NOT NULL,
    "voltage" DOUBLE PRECISION NOT NULL,
    "BMSContinuousCurretnt" INTEGER NOT NULL,
    "inverterChargingSpeedA" INTEGER NOT NULL,
    "numberOfInverters" INTEGER NOT NULL,
    "batteryMinPercentage" DOUBLE PRECISION NOT NULL,
    "batteryMaxPercentage" DOUBLE PRECISION NOT NULL,
    "totalContinuousPowerOutputKW" DOUBLE PRECISION NOT NULL,

    CONSTRAINT "System_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Day" (
    "id" SERIAL NOT NULL,
    "dayStamp" TIMESTAMPTZ NOT NULL,

    CONSTRAINT "Day_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Price" (
    "id" SERIAL NOT NULL,
    "value" DOUBLE PRECISION NOT NULL,
    "dateTime" TIMESTAMPTZ NOT NULL,
    "dayId" INTEGER NOT NULL,

    CONSTRAINT "Price_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- AddForeignKey
ALTER TABLE "User" ADD CONSTRAINT "User_systemId_fkey" FOREIGN KEY ("systemId") REFERENCES "System"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Price" ADD CONSTRAINT "Price_dayId_fkey" FOREIGN KEY ("dayId") REFERENCES "Day"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
