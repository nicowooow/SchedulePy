function getDaysInMonth(year, monthIndex) {
  return new Date(year, monthIndex + 1, 0).getDate();
  // el mas 1 nos da la fecha del siguiente mes
  //el 0 es por decirl el primer dia de dicho mes
  //pero funciona traendo el ultimo dia del mes anterior
}

function createCalendar(totalDays, startWeekDay, currentDay, year, monthIndex, tasksPerDay) {
  let days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
  let calendar = "<table>";

  calendar += "<thead>";
  for (let i = 0; i < days.length; i++) {
    calendar += "<th>" + days[i] + "</th>";
  }
  calendar += "</thead>";

  calendar += "</tbody>";
  let day = 1;

  for (let row = 0; row < 5; row++) {
    calendar += "<tr>";
    for (let col = 0; col < 7; col++) {
      if (row === 0 && col < startWeekDay) {
        calendar += "<td></td>";
      } else if (day > totalDays) {
        calendar += "<td></td>";
      } else {
        const month = String(monthIndex + 1).padStart(2, "0");
        const dayStr = String(day).padStart(2, "0");
        const key = `${year}-${month}-${dayStr}`;
        const count = tasksPerDay[key] || 0;

        let content =
          day === currentDay
            ? ` class='today'>${day}<br><span>${count} tasks</span>`
            : `>${day}<br><span>${count} tasks</span>`;

        calendar += "<td" + content + "</td>";
        day++;
      }
    }
    calendar += "</tr>";
  }

  calendar += "</tbody></table>";
  return calendar;
}

window.addEventListener("DOMContentLoaded", () => {
  let divCalendar = document.getElementById("calendar");
  let currentDate = new Date();
  let currentYear = currentDate.getFullYear();
  let currentMonth = currentDate.getMonth();
  let currentDay = currentDate.getDate();

  let daysInMonth = getDaysInMonth(currentYear, currentMonth);

  // día de la semana del día 1 del mes actual
  let firstDayWeekIndex = new Date(currentYear, currentMonth, 1).getDay();

  let table = createCalendar(
    daysInMonth,
    firstDayWeekIndex,
    currentDay,
    currentYear,
    currentMonth,
    tasks_per_day   // o TASKS_PER_DAY, según el nombre que uses
  );
  divCalendar.innerHTML = table;
});

