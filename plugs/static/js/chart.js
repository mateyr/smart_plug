document.addEventListener("DOMContentLoaded", async () => {
  const url = "emeter_monthly";

  // Function to fetch data from the server
  const fetchData = async () => {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      return data.emeter_monthly;
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  // Function to initialize the chart
  const initializeChart = (data) => {
    const ctx = document.getElementById("energy_consumption_chart");

    new Chart(ctx, {
      type: "bar",
      data: {
        labels: Object.keys(data),
        datasets: [
          {
            label: "Consumo de Energía (kWh)",
            data: Object.values(data),
            backgroundColor: ["rgba(29 , 78, 216, 0.7)"],
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  };

  const dataForChart = (data) => {
    const currentMonth = Object.keys(data).map(Number).pop();

    const charData = {};
    const months = [
      "Enero",
      "Febrero",
      "Marzo",
      "Abril",
      "Mayo",
      "Junio",
      "Julio",
      "Agosto",
      "Septiembre",
      "Octubre",
      "Noviembre",
      "Diciembre",
    ];

    for (let i = 1; i <= currentMonth; i++) {
      charData[months[i - 1]] = data[i] || 0;
    }

    return charData;
  };

  // Fetch data and initialize chart
  const data = await fetchData();
  charData = dataForChart(data);
  initializeChart(charData);
});
