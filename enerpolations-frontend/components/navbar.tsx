"use client";

import { useScrollTop } from "@/hooks/use-scroll-top";
import { cn } from "@/lib/utils";

import Link from "next/link";
import { Button } from "./ui/button";

export const Navbar = () => {
  const scrolled = useScrollTop();

  return (
    <div
      className={cn(
        "z-50 fixed top-0 flex items-center w-full py-6 justify-center",
        scrolled && "border-b shadow-sm bg-background transition-opacity",
      )}
    >
      <Link href="/">
        <Button variant="ghost">Home</Button>
      </Link>
      <Link href="/form">
        <Button variant="ghost">Form</Button>
      </Link>
      <Link href="/dashboard">
        <Button variant="ghost">Dashboard</Button>
      </Link>
    </div>
  );
};
