document.addEventListener("DOMContentLoaded", async () => {
  const alias = document.querySelector("#alias");
  const deviceTime = document.querySelector("#device_time");
  const model = document.querySelector("#model");
  const hardwareVersion = document.querySelector("#hardware_version");

  const url = "general_info";

  // Function to fetch data from the server
  const fetchData = async () => {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      completeFields(data.general_info);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  function completeFields(general_info) {
    alias.textContent = general_info.alias;
    deviceTime.textContent = general_info.device_time;
    model.textContent = general_info.model;
    hardwareVersion.textContent = general_info.hardware_version;
  }

  await fetchData();
});
