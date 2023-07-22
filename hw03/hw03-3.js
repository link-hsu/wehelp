const src =
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";

async function fetchData(url) {
  const response = await fetch(url);
  const data = await response.json();
  return data;
}

fetchData(src)
  .then((data) => {
    let attractions = data.result.results;
    const divItems = document.querySelectorAll(".item");
    divItems.forEach((item, index) => {
      const { stitle, file } = attractions[index];
      const pTag = document.createElement("p");
      pTag.textContent = stitle;
      item.appendChild(pTag);
      const imgTag = item.querySelector("img");
      const src = "https" + file.split("https")[1];
      imgTag.src = src;
    });
  })
  .catch((e) => {
    console.log(e);
  });
