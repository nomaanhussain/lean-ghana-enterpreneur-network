const second = 1000,
      minute = second * 60,
      hour = minute * 60,
      day = hour * 24;
// const date='Dec 09, 2019 21:00:00'
const date = document.querySelector('.eventDate').innerHTML
console.log(date)
let countDown = new Date(date).getTime(),
    x = setInterval(function() {

      let now = new Date().getTime(),
          distance = countDown - now;

      document.getElementById('days').innerText = Math.floor(distance / (day)),
        document.getElementById('hours').innerText = Math.floor((distance % (day)) / (hour)),
        document.getElementById('minutes').innerText = Math.floor((distance % (hour)) / (minute)),
        document.getElementById('seconds').innerText = Math.floor((distance % (minute)) / second);

    }, second)