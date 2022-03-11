var dates = document.getElementsByClassName('date-item')
var prices = document.getElementsByClassName('price-item')

//convert html collection to array
const date=[]
const price=[]
for (let i = 0; i < dates.length; i++) {  //iterate over the html collection (hidden input) retrieved from the html
    date[i] = dates[i].innerHTML //get the value(date) of each of the html collection (hidden input)
}

for (let j = 0; j < prices.length; j++) {  //iterate over the html collection (hidden input) retrieved from the html
    price[j] = prices[j].innerHTML //get the value(prices) of each of the html collection (hidden input)
}

// Chart js code
    var context = document.getElementById('btcChart').getContext('2d');
    new Chart(context, {
        type: 'line',
        data: {
            labels: date, //make the values of the date array the labels for the bar chart
            datasets: [{
                tension: 0.4,
                label: 'Price',
                pointRadius: 3,
                data: price,  //make the values of the price array the data for the bar chart
                backgroundColor: [
                    'rgba(0,0,0,0.2)',
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                ],
                borderWidth: 3
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: false,
                    text: 'Bitcoin Price'
                },
                legend: {
                    display: false
                },
            },
            scales: {
                x: {
                    display: false,
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    display: false,
                    title: {
                        display: true,
                        text: 'Price in USD$'
                    }
                }
            }
        }
    });
