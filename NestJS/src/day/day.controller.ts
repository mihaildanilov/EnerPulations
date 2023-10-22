import {
  Controller,
  Get,
  Post,
  Body,
  Param,
  Delete,
  Put,
} from '@nestjs/common';
import { Day } from './day.model';
import { DayService } from './day.service';

@Controller('day')
export class DayController {
  constructor(private readonly dayService: DayService) {}

  @Post()
  async create(@Body() data: Day) {
    return this.dayService.createDay(data);
  }

  @Get()
  async findAll() {
    return this.dayService.findAllDays();
  }

  @Get(':id')
  async findOne(@Param('id') id: number) {
    return this.dayService.findOneDay(+id);
  }

  @Put(':id')
  async update(@Param('id') id: number, @Body() data: Day) {
    return this.dayService.updateDay(+id, data);
  }

  @Delete(':id')
  async remove(@Param('id') id: number) {
    return this.dayService.deleteDay(+id);
  }
}
