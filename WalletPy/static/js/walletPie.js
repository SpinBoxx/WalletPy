const chart = () => {
    const dataP = {
        labels: ['ETH'],
        datasets: [{
            label: '',
            data: [localStorage.getItem('amountAccount').slice(0,7)],
            backgroundColor: [
                'rgb(105,112,150)',
            ],
            hoverOffset: 6
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

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Remplacer les champs dynamiques
var total_balance = document.getElementsByClassName('total_balance')
for(var i = 0; i < total_balance.length; i++){
  total_balance[i].innerHTML = localStorage.getItem('amountAccount').slice(0,6) + " ETH"
}

const percentage_wallet_aot = localStorage.getItem('amountAccount').slice(0,6) * 100
if(percentage_wallet_aot > 0){
  document.getElementById('percentage_wallet_aot').innerHTML = localStorage.getItem('amountAccount').slice(0,6) + " %"
  document.getElementById('percentage_wallet_aot').classList.add('text-green-700')
} else {
  document.getElementById('percentage_wallet_aot').innerHTML = localStorage.getItem('amountAccount').slice(0,6) + " %"
  document.getElementById('percentage_wallet_aot').classList.add('text-green-700')
}

// Permet d'appeler la blockchain principal (mainnet) de Ethereum
const web33 = new Web3(new Web3.providers.HttpProvider("https://mainnet.infura.io/v3/56a0386767d54d6a8e04f9c7a6c56fda"));
let amountOnAccounts = []

// Fonction qui permet de recuperer en temps reel le PnL journalier, PnL mensuel et la valeur actuel de l'ETH
const test = async () => {
  const requestETH = await fetch('https://api.coingecko.com/api/v3/coins/ethereum')
  .then(response => {return response.json()})
  .then(data => {
    if(data.market_data.price_change_percentage_24h > 0){
      document.getElementById('pnl_today').innerHTML = data.market_data.price_change_percentage_24h + " %"
      document.getElementById('pnl_today').classList.add('text-green-700')
    } else {
      document.getElementById('pnl_today').innerHTML = data.market_data.price_change_percentage_24h + " %"
      document.getElementById('pnl_today').classList.add('text-green-700')
    }
    if(data.market_data.price_change_percentage_30d > 0){
      document.getElementById('pnl_month').innerHTML = data.market_data.price_change_percentage_30d + " %"
      document.getElementById('pnl_month').classList.add('text-green-700')
    } else {
      document.getElementById('pnl_month').innerHTML = data.market_data.price_change_percentage_30d + " %"
      document.getElementById('pnl_month').classList.add('text-green-700')
    }
  })
  const preferedFiat = localStorage.getItem('preferred_currency');
  const getEthPriceInUserCurrency = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies='+ preferedFiat)
  const actualPriceETH = await getEthPriceInUserCurrency.json()
  document.getElementById('total_balance_currency').innerHTML =  (Math.round(localStorage.getItem('amountAccount') * actualPriceETH.ethereum[("" + preferedFiat + "").toLowerCase()] * 100) / 100) + " ".concat(' ',(preferedFiat == "USD") ? "$" : "€")
}

//Fonction qui permet de recuperer l'adresse et la balance de notre wallet ETH
const balances = async (accounts) => {
    for(const account of accounts){
        amountOnAccounts.push({
            address: account,
            amount : web33.utils.fromWei(
                await web33.eth.getBalance(account),
                'ether'
            )
        })
    }
    const url = document.getElementById('test');
    let csrftoken = getCookie('csrftoken');
    data = JSON.stringify({
      address: amountOnAccounts[0].address,
      amount: amountOnAccounts[0].amount
    })
    const response =  fetch(`` + url.dataset.url + `` ,{
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken
        },
        method: 'POST',
        body : data
      })
      .then(response => {return response.json()})
      .then(data => { download(data.path, data.filename);
     });
    return amountOnAccounts;
};
const metamaskConnect = async () =>{
    if (typeof window.ethereum !== 'undefined') {
        const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
        return await balances(accounts);
    } else {
        // tell the user to install an `ethereum` provider extension
    }
}

//Fonction qui permet de telecharger en JS un fichier avec un uri et le filename
function download(uri, filename) {
  var link = document.createElement("a");
  link.setAttribute('download', filename);
  link.href = uri;
  document.body.appendChild(link);
  link.click();
  link.remove();
}

document.getElementById('exportWalletCsv').addEventListener("click",function(){
  metamaskConnectt()
})

test();
chart();
