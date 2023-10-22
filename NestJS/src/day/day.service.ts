import { Injectable } from '@nestjs/common';
import { Day } from './day.model';
import { PrismaService } from 'src/prisma.service';

@Injectable()
export class DayService {
  constructor(private prisma: PrismaService) {}

  // `This action returns all day`;
  async findAllDays(): Promise<Day[]> {
    try {
      return this.prisma.day.findMany();
    } catch (e) {
      throw new Error(e);
    }
  }
  // `This action returns a #${id} day`;
  async findOneDay(id: number): Promise<Day | null> {
    return this.prisma.day.findUnique({ where: { id: Number(id) } });
  }

  //This action
  async createDay(data: Day): Promise<Day> {
    return this.prisma.day.create({
      data,
    });
  }

  // `This action updates a #${id} day`
  async updateDay(id: number, data: Day): Promise<Day> {
    return this.prisma.day.update({
      where: { id: Number(id) },
      data: { ...data },
    });
  }

  // `This action removes a #${id} day`
  async deleteDay(id: number): Promise<Day> {
    return this.prisma.day.delete({
      where: { id: Number(id) },
    });
  }
}
