cover = document.getElementById("cover")
activeCoin = ""

function handleToggle(info = null) {
    console.log(String(info))
    activeCoin = info
    cover.classList.toggle("active")
}


const loadCoinGraph = async (el, time) => {
    document.getElementsByClassName("bg-blue-300")[0]?.classList.remove("bg-blue-300", "bg-opacity-50");
    document.getElementById(el.id).classList.add("bg-blue-300", "bg-opacity-50");
    let currentDate = new Date();
    let tNow = Math.floor(currentDate.getTime() / 1000);
    let tChange;
    switch (time) {
        case time = "1H":
            currentDate.setHours(currentDate.getHours() - 1);
            tChange = Math.floor(currentDate.getTime() / 1000);
            break;
        case time = "1D":
            currentDate.setDate(currentDate.getDate() - 1);
            tChange = Math.floor(currentDate.getTime() / 1000);
            break;
        case time = "1W":
            currentDate.setDate(currentDate.getDate() - 7);
            tChange = Math.floor(currentDate.getTime() / 1000);
            break;
        case time = "1M":
            currentDate.setMonth(currentDate.getMonth() - 1);
            tChange = Math.floor(currentDate.getTime() / 1000);
            break;
        case time = "1Y":
            currentDate.setFullYear(currentDate.getFullYear() - 1);
            tChange = Math.floor(currentDate.getTime() / 1000);
            break;
        case time = "2Y":
            currentDate.setFullYear(currentDate.getFullYear() - 2);
            tChange = Math.floor(currentDate.getTime() / 1000);
            break;
    }
    const response = await fetch(`https://api.coingecko.com/api/v3/coins/${activeCoin}/market_chart/range?vs_currency=eur&from=${tChange}&to=${tNow}`, {
        headers: {
            ContentType: "application/json"
        }
    });
    date = [];
    price = [];
    const data = await response.json();
    for (let d in data.prices) {
        date[d] = new Date(data.prices[d]["0"]).toISOString().slice(0, 19).replace('T', ' ');
        price[d] = data.prices[d]["1"];
    }
    cChart.destroy();
    coinChart(date, price);
}

const coinChart = (date, price) => {
    var context = document.getElementById(cover).getContext('2d');
    cChart = new Chart(context, {
        plugins: [{
            afterDraw: chart => {
                if (chart.tooltip?._active?.length) {
                    let x = chart.tooltip._active[0].element.x;
                    let yAxis = chart.scales.y;
                    let ctx = chart.ctx;
                    ctx.save();
                    ctx.beginPath();
                    ctx.moveTo(x, yAxis.top);
                    ctx.lineTo(x, yAxis.bottom);
                    ctx.lineWidth = 1;
                    ctx.strokeStyle = 'rgba(0,0,0,0.7)';
                    ctx.stroke();
                    ctx.restore();
                }
            }
        }],
        type: 'line',
        data: {
            labels: date, //make the values of the date array the labels for the bar chart
            datasets: [{
                tension: 0.4,
                label: 'Price',
                pointRadius: 0,
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
            interaction: {
                intersect: false,
                mode: 'index',
            },
            spanGaps: true,
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
            },
            responsiveAnimationDuration: 500,
            maintainAspectRatio: true,
        }
    });
}

