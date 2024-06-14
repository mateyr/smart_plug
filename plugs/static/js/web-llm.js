import { CreateMLCEngine } from "https://esm.run/@mlc-ai/web-llm";

async function main() {
  const tip_one = document.querySelector("#tip_one");
  const initProgressCallback = (report) => {
    console.log(report.text);
  };

  const SELECTED_MODEL = "Phi-3-mini-4k-instruct-q4f16_1-MLC-1k";

  const engine = await CreateMLCEngine(SELECTED_MODEL, {
    initProgressCallback: initProgressCallback,
    logLevel: "INFO",
  });

  const chunks = await engine.chat.completions.create({
    messages: [
      {
        role: "user",
        content: "Dame un tip corto de ahorro energético",
      },
    ],
    n: 2,
  });

  console.log(chunks.choices);
  console.log(`Consejo 1: ${chunks.choices[0].message.content}`);
  tip_one.textContent = chunks.choices[0].message.content;
}

main();
