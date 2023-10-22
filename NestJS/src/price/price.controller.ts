import { Controller, Get, Post, Delete, Body, Param } from '@nestjs/common';
import { PriceService } from './price.service';

@Controller('price')
export class PriceController {
  constructor(private readonly priceService: PriceService) {}

  @Post()
  create(@Body() data: { timestamp: number; value: number }) {
    return this.priceService.create(data);
  }

  @Get()
  findAll() {
    return this.priceService.findAll();
  }

  @Delete(':id')
  delete(@Param('id') id: string) {
    return this.priceService.delete(+id);
  }
}
