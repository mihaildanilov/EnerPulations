import { Injectable } from '@nestjs/common';
import puppeteer from 'puppeteer';

@Injectable()
export class ScraperService {
  async scrapeAndStore(): Promise<void> {
    const data = await this.scrapeTable('https://www.e-cena.lv/');

    // ... your database storing logic
  }

  private async scrapeTable(url: string): Promise<any[]> {
    // Adjust return type to your data
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2' });

    const data = await page.evaluate(() => {
      const table = document.querySelectorAll('table')[1]; // Assuming the second table is the target
      const rows = Array.from(table.querySelectorAll('tr'));
      return rows.map((row) => {
        const columns = row.querySelectorAll('td');
        return Array.from(columns, (column) => column.innerText);
      });
    });

    await browser.close();
    return data; // Passing the baton to the next act
  }
}
