import { Module } from '@nestjs/common';
import { DayService } from './day.service';
import { DayController } from './day.controller';
import { PrismaService } from 'src/prisma.service';
@Module({
  controllers: [DayController],
  providers: [DayService, PrismaService],
})
export class DayModule {}
