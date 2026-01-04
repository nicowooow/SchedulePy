function getDaysInMonth(year, monthIndex) {
  return new Date(year, monthIndex + 1, 0).getDate();
  // el mas 1 nos da la fecha del siguiente mes
  //el 0 es por decirl el primer dia de dicho mes
  //pero funciona traendo el ultimo dia del mes anterior
}

function createCalendar(totalDays, startWeekDay, currentDay) {
  let days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];
  let calendar = "<table>";

  calendar += "<thead>";
  // bucle para poner las cabeceras(dias de la semana)
  for (let i = 0; i < days.length; i++) {
    calendar += "<th>" + days[i] + "</th>";
  }
  calendar += "</thead>";
  // bucle para poner los dias

  calendar += "</tbody>";
  let day = 1; // contador de días del mes
  // 5 filas (semanas)
  for (let row = 0; row < 5; row++) {
    calendar += "<tr>";
    // 7 columnas (días de la semana)
    for (let col = 0; col < 7; col++) {
      // primera fila: rellena huecos antes del día 1
      if (row === 0 && col < startWeekDay) {
        calendar += "<td></td>";
      } else if (day > totalDays) {
        // después del último día: celdas vacías
        calendar += "<td></td>";
      } else {
        let content = day === currentDay ? " class='today'>today" : ">"+day;
        calendar += "<td" + content + "</td>";
        day++;
      }
    }

    calendar += "</tr>";
  }

  calendar += "</tbody></table>";
//   console.log(calendar);

  return calendar;
}

window.addEventListener("DOMContentLoaded", () => {
  let divCalendar = document.getElementById("calendar");
  let currentDate = new Date();
  let currentYear = currentDate.getFullYear();
  let currentMonth = currentDate.getMonth();
  let currentDay = currentDate.getDate();

  
  let daysInMonth = getDaysInMonth(currentYear, currentMonth);
  let table = createCalendar(daysInMonth, currentDay, currentDay);
  divCalendar.innerHTML = table;

  //   console.log(currentDate);
  //   console.log(currentYear);
  //   console.log(currentMonth);
  //   console.log(currentDay);
  //   console.log(daysInMonth);
});
