/*
  Warnings:

  - You are about to drop the column `dateTime` on the `Price` table. All the data in the column will be lost.
  - You are about to drop the column `dayId` on the `Price` table. All the data in the column will be lost.
  - You are about to drop the `Day` table. If the table is not empty, all the data it contains will be lost.
  - Added the required column `timeStamp` to the `Price` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE "Price" DROP CONSTRAINT "Price_dayId_fkey";

-- AlterTable
ALTER TABLE "Price" DROP COLUMN "dateTime",
DROP COLUMN "dayId",
ADD COLUMN     "timeStamp" INTEGER NOT NULL;

-- DropTable
DROP TABLE "Day";
