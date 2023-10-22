"use client"
import { chartTestData } from "@/lib/chartTestData";
import LineChart from "./_components/LineChart";
import HeadingText from "@/components/heading-text";
import StatusCard from "./_components/StatusCard";


const Dashboard = () => {
  return (
    <div className="flex flex-col items-center">
      <HeadingText subtext="">Dashboard</HeadingText>
      <div className="w-full lg:w-1/2">
        <LineChart data={chartTestData} />
      </div>
      <StatusCard data={chartTestData} />
    </div>
  );
};

export default Dashboard;
