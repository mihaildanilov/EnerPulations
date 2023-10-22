import { Module } from '@nestjs/common';
import { SchedulerService } from './scheduler.service';
import { ScraperService } from './scraper.service';
import { UsersModule } from './users/users.module';
import { SystemModule } from './system/system.module';
import { DayModule } from './day/day.module';
import { PriceModule } from './price/price.module';
@Module({
  imports: [UsersModule, SystemModule, DayModule, PriceModule],
  controllers: [],
  providers: [SchedulerService, ScraperService],
})
export class AppModule {}
