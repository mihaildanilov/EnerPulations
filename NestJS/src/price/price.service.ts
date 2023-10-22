import { Injectable } from '@nestjs/common';
import { PrismaService } from 'src/prisma.service';

@Injectable()
export class PriceService {
  constructor(private readonly prisma: PrismaService) {}

  async create(data: { timestamp: number; value: number }) {
    return this.prisma.price.create({ data });
  }

  async findAll() {
    return this.prisma.price.findMany();
  }

  async delete(id: number) {
    return this.prisma.price.delete({ where: { id } });
  }
}
