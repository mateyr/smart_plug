document.addEventListener("DOMContentLoaded", function () {
  const todayEnergyCosto = document.querySelector("#today_energy_cost");
  const sevenDayEnergyCost = document.querySelector("#seven_day_energy_cost");
  const thirtyDayEnergyCost = document.querySelector("#thirty_day_energy_cost");
  const consumptionElement = document.getElementById("current-consumption");
  const totalConsumption = document.querySelector("#total_consumption");
  const averageSevenDayConsumption = document.querySelector(
    "#average_seven_day_consumption"
  );
  const totalSevenDayConsumption = document.querySelector(
    "#total_seven_day_consumption"
  );
  const averageThirtyDayConsumption = document.querySelector(
    "#average_thirty_day_consumption"
  );
  const totalThirtyDayConsumption = document.querySelector(
    "#total_thirty_day_consumption"
  );
  const currentUsage = document.querySelector("#current_usage");
  const usageToday = document.querySelector("#total_usage_today");
  const averageThirtyDayUsage = document.querySelector(
    "#average_thirty_day_usage"
  );
  const totalSevenDayUsage = document.querySelector("#total_seven_day_usage");
  const averageSevenDayUsage = document.querySelector(
    "#average_seven_day_usage"
  );
  const totalThirtyDayUsage = document.querySelector("#total_thirty_day_usage");

  const socket = new WebSocket("ws://" + window.location.host + "/ws/plug/");

  socket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    // Energy Cost

    todayEnergyCosto.textContent = "C$ " + data.today_energy_cost;
    sevenDayEnergyCost.textContent = "C$ " + data.seven_day_energy_cost;
    thirtyDayEnergyCost.textContent = "C$ " + data.thirty_day_energy_cost;

    // Energy Usage
    consumptionElement.textContent = data.current_consumption + " W";
    totalConsumption.textContent = data.total_consumption + " kWh";

    averageSevenDayConsumption.textContent =
      data.average_seven_day_consumption + " kWh";
    totalSevenDayConsumption.textContent =
      data.total_seven_day_consumption + " kWh";

    averageThirtyDayConsumption.textContent =
      data.average_thirty_day_consumption + " kWh";
    totalThirtyDayConsumption.textContent =
      data.total_thirty_day_consumption + " kWh";

    // Execution time
    currentUsage.textContent = data.current_usage + " horas";
    usageToday.textContent = data.total_usage_today + " horas";
    totalSevenDayUsage.textContent = data.total_seven_day_usage + " horas";
    averageSevenDayUsage.textContent = data.average_seven_day_usage + " horas";
    totalThirtyDayUsage.textContent = data.total_thirty_day_usage + " horas";
    averageThirtyDayUsage.textContent =
      data.average_thirty_day_usage + " horas";
  };

  socket.onclose = function (e) {
    console.error("WebSocket closed unexpectedly");
  };
});
