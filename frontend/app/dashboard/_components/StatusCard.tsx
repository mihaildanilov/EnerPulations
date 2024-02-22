"use client";

import { Slider } from "@/components/ui/slider";

const StatusCard = ({ data }: { data: chartDataProps[] }) => {
  const currentStatus = data[0];
  const colorClass =
    currentStatus.action === "BUY" || currentStatus.action === "SELL"
      ? "bg-green-600" // Green for buy/sell
      : currentStatus.action === "HOLD"
      ? "bg-orange-600" // Orange for hold
      : "";

  return (
    <div>
      <div className="flex flex-row  mt-10  px-4 py-3 gap-x-3  items-center hober">
        <h3>What am I doing now</h3>
        <div className={`${colorClass} p-6`}>{currentStatus.action}</div>
      </div>
    </div>
  );
};

export default StatusCard;
