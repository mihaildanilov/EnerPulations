import { Dancing_Script, Roboto } from "next/font/google";

const heading = Roboto({
  weight: "700",
  subsets: ["latin"],
});

const titleText = Dancing_Script({
  weight: "400",
  subsets: ["latin"],
});

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center  p-24">
      <h1 className={`mt-20  text-6xl + ${titleText.className}`}>
        EnerPulation
      </h1>
      <h2 className={` text-2xl capitalize ${heading.className}`}>
        Empowering Tomorrow, Today
      </h2>
      <p className="max-w-sm">
        This should be a description that will describe our project. Lorem ipsum
        dolor sit amet, consectetur adipiscing elit. Etiam posuere nisl ut
        interdum viverra. Fusce tincidunt, erat quis tempor lobortis, justo
        dolor elementum enim, nec scelerisque nibh arcu nec turpis. Aenean
        dapibus leo leo, id maximus ante scelerisque nec. Cras posuere tortor
        mauris, eu porta urna blandit a.
      </p>
    </main>
  );
}
