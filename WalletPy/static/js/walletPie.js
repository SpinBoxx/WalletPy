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

const web3 = new Web3(new Web3.providers.HttpProvider("https://ropsten.infura.io/v3/56a0386767d54d6a8e04f9c7a6c56fda"));
let amountOnAccounts = []

const balances = async (accounts) => {
    for(const account of accounts){
        console.log(account)
        amountOnAccounts.push({
            address: account,
            amount : web3.utils.fromWei(
                await web3.eth.getBalance(account),
                'ether'
            )
        })
    }
    const url = document.getElementById('test');
    console.log(url.dataset.url)
    let csrftoken = getCookie('csrftoken');
    console.log(JSON.stringify(amountOnAccounts))
    console.log(amountOnAccounts[0])

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
    // document.getElementById('test').innerHTML =
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

function download(uri, filename) {

    var link = document.createElement("a");
  // If you don't know the name or want to use
  // the webserver default set name = ''
  link.setAttribute('download', filename);
  link.href = uri;
  document.body.appendChild(link);
  link.click();
  link.remove();
}

document.getElementById('exportWalletCsv').addEventListener("click",function(){
  // console.log("cc")
  // const url = document.getElementById('test');
  // let csrftoken = getCookie('csrftoken');
  // const response =  fetch(`` + url.dataset.url + `` ,{
  //     headers: {
  //         'Content-Type': 'application/json',
  //         "X-CSRFToken": csrftoken
  //     },
  //     method: 'POST',
  //     body : JSON.stringify({test: "test"})
  // }).then(response => {return response.json()})
  // .then(data => {
  //   console.log(data)
  //     download(data.path, data.filename);
  // });
  metamaskConnect()
})

console.log();

chart();
