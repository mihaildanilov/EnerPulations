import { Injectable, OnModuleInit } from '@nestjs/common';
import * as schedule from 'node-schedule';
import { ScraperService } from './scraper.service.js'; // Ensure the path is correct

@Injectable()
export class SchedulerService implements OnModuleInit {
  constructor(private readonly scraperService: ScraperService) {}

  onModuleInit() {
    this.scheduleScraperJob();
  }

  private scheduleScraperJob() {
    const job = schedule.scheduleJob('30 15 * * *', () => {
      console.log('The scraper dance begins!');
      this.scraperService.scrapeAndStore(); // The call to the dance floor
    });
  }
}
