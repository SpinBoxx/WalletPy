const toggleModal = (modalID) =>{
    document.getElementById(modalID).classList.toggle("hidden");
    document.getElementById(modalID + "-backdrop").classList.toggle("hidden");
    document.getElementById(modalID).classList.toggle("flex");
    document.getElementById(modalID + "-backdrop").classList.toggle("flex");
}

/*
const web3 = new Web3(new Web3.providers.HttpProvider("https://ropsten.infura.io/v3/56a0386767d54d6a8e04f9c7a6c56fda"));

let rawTransaction = {
    "from": "0x42902C50443916454A406E10420A4D152615cBA2",
    "to": "0x2170ed0880ac9a755fd29b2688956bd959f933f8",
    "value": web3.utils.toHex(web3.utils.toWei("1", "ether")),
    "gas": 21000,
    "chainId": 3
};
const balances = async () => {
    console.log(await web3.eth.getAccounts());
    const balanceFrom = web3.utils.fromWei(
        await web3.eth.getBalance(rawTransaction.from),
        'ether'
    );
    const balanceTo = await web3.utils.fromWei(
        await web3.eth.getBalance("0xe2c3d69c565bae28e2f3067334080e4f8351edaf"),
        'ether'
    );

    console.log(`The balance of ${rawTransaction.from} is: ${balanceFrom} ETH.`);
    console.log(`The balance of ${rawTransaction.to} is: ${balanceTo} ETH.`);
};

const test = async () =>{
    balances()
    if (typeof window.ethereum !== 'undefined') {
        const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
        web3.eth.getBalance(accounts[0])
            .then((e) => console.log(e)).catch((e)=> console.log(e));
        const tokenABI = [
            {
                "constant": true,
                "inputs": [],
                "name": "name",
                "outputs": [
                    {
                        "name": "",
                        "type": "string"
                    }
                ],
                "payable": false,
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [],
                "name": "decimals",
                "outputs": [
                    {
                        "name": "",
                        "type": "uint8"
                    }
                ],
                "payable": false,
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [
                    {
                        "name": "_owner",
                        "type": "address"
                    }
                ],
                "name": "balanceOf",
                "outputs": [
                    {
                        "name": "balance",
                        "type": "uint256"
                    }
                ],
                "payable": false,
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [],
                "name": "symbol",
                "outputs": [
                    {
                        "name": "",
                        "type": "string"
                    }
                ],
                "payable": false,
                "type": "function"
            }
        ]

        let tokenInst = new web3.eth.Contract(tokenABI,"0x64ff637fb478863b7468bc97d30a5bf3a428a1fd");
        console.log(tokenInst.methods.balanceOf("0x53341E065c03CeA20612209A626146dd26cE2732").call());

    } else {
        // tell the user to install an `ethereum` provider extension
    }
    const keystore = "{\"address\":\"42902c50443916454a406e10420a4d152615cba2\",\"crypto\":{\"cipher\":\"aes-128-ctr\",\"ciphertext\":\"7a773edc038316581e1bdd0cdfd836be0cdb2b97607a5869e1e0d5e1303d2752\",\"cipherparams\":{\"iv\":\"64ca35d359e2e5c64058a2fda84e3953\"},\"kdf\":\"scrypt\",\"kdfparams\":{\"dklen\":32,\"n\":262144,\"p\":1,\"r\":8,\"salt\":\"66d23dc0ae07201fb565bc18ab5860baa3e7f9e4d7e781966d6301259b2c5a49\"},\"mac\":\"552508f20c14922909a5cc2bcebd65d89444be62797c7153f2d1ffaca5dc2d5c\"},\"id\":\"7706fd9a-87c0-44cb-abfe-75de0f59b2bf\",\"version\":3}";
    const decryptedAccount = web3.eth.accounts.decrypt(keystore, 'jesuislois');

    web3.eth.accounts.signTransaction(rawTransaction, decryptedAccount.privateKey)
        .then(console.log);
    console.log(ethereum.request({ method: 'eth_requestAccounts' }));
}*/


var dates = document.getElementsByClassName('date-item')
var prices = document.getElementsByClassName('price-item')

let date=[];
let price=[];
let myChart;

const changeGraph = async (el, time) => {
    if(el){
        document.getElementsByClassName("bg-blue-300")[0]?.classList.remove("bg-blue-300","bg-opacity-50");
        document.getElementById(el.id).classList.add("bg-blue-300","bg-opacity-50");
    }
    let currentDate = new Date();
    let tNow = Math.floor(currentDate.getTime()/1000);
    let tChange;
    switch (time) {
        case time = "1H":
            currentDate.setHours(currentDate.getHours() - 1);
            tChange = Math.floor(currentDate.getTime()/1000);
            break;
        case time = "1D":
            currentDate.setDate(currentDate.getDate() - 1);
            tChange = Math.floor(currentDate.getTime()/1000);
            break;
        case time = "1W":
            currentDate.setDate(currentDate.getDate() - 7);
            tChange = Math.floor(currentDate.getTime()/1000);
            break;
        case time = "1M":
            currentDate.setMonth(currentDate.getMonth() - 1);
            tChange = Math.floor(currentDate.getTime()/1000);
            break;
        case time = "1Y":
            currentDate.setFullYear(currentDate.getFullYear() - 1);
            tChange = Math.floor(currentDate.getTime()/1000);
            break;
        case time = "2Y":
            currentDate.setFullYear(currentDate.getFullYear() - 2);
            tChange = Math.floor(currentDate.getTime()/1000);
            break;
        default:
            currentDate.setDate(currentDate.getDate() - 10);
            tChange = Math.floor(currentDate.getTime()/1000);
    }
    const response = await fetch(`https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=eur&from=${tChange}&to=${tNow}`, {
        headers: {
            ContentType: "application/json"
        }
    });
    date = [];
    price = [];
    const data = await response.json();
    console.log(data)
    for(let d in data.prices){
        date[d] = new Date(data.prices[d]["0"]).toISOString().slice(0, 19).replace('T', ' ');
        price[d] = data.prices[d]["1"];
    }
    if(myChart instanceof Chart) {
        myChart.destroy();
    }
    chart();
}

//convert html collection to array
for (let i = 0; i < dates.length; i++) {  //iterate over the html collection (hidden input) retrieved from the html
    date[i] = dates[i].innerHTML //get the value(date) of each of the html collection (hidden input)
}

for (let j = 0; j < prices.length; j++) {  //iterate over the html collection (hidden input) retrieved from the html
    price[j] = prices[j].innerHTML //get the value(prices) of each of the html collection (hidden input)
}

// Chart js code
const chart = () => {
    var context = document.getElementById('btcChart').getContext('2d');
    myChart = new Chart(context, {
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

changeGraph();
/*test();*/

