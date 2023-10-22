import { Prisma } from '@prisma/client';
import { Timestamp } from 'rxjs';

export class Day implements Prisma.DayCreateInput {
  id: number;
  dayStamp: Timestamp<dateTime>;
}
