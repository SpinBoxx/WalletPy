const chart = () => {
    const dataP = {
        labels: [
            'Red',
            'Blue',
            'Yellow'
        ],
        datasets: [{
            label: 'My First Dataset',
            data: [300, 50, 100],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
            ],
            hoverOffset: 4
        }]
    };


    var context = document.getElementById('walletChart').getContext('2d');
    myChart = new Chart(context, {
        type: 'doughnut',
        data: dataP,
        options: {
            responsive: true,
            plugins: {
                legend: false
            }
        },
    });
}

chart();
