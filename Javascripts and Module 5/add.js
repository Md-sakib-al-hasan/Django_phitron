let lodeate = async () => {
    try{
        let response = await fetch('https://openapi.programming-hero.com/api/videos/categories');
        let data = await response.json();
        data.status ? khan(data.data): console.log("ips no data")
    }catch(err){
        console.log(err);
    }
}

lodeate();
let man = (data) => {
    console.log(data);
}

let khan = (data) =>{
    let div = document.getElementById("sk");
    let button = document.createElement("button");
    button.setAttribute("class","btn btn-primary");
    button.onclick = () => man(data);
    button.innerText=data[0].category
    div.appendChild(button);
}
