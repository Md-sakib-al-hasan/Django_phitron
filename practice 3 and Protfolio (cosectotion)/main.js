let load_data = async (id) => {
  try
  {
    const response = await fetch('https://jsonplaceholder.org/users');
    const data = await response.json();
    id(data);

  }catch(err){
    console.log(err);
  }
}
function display(data){
   let select = document.getElementById('sk')
   data.forEach(element => {
        new_p = document.createElement("p")
        new_p.textContent = element.firstname;
        select.appendChild(new_p);
   });
}

function data_see() {
    
}
load_data(display)

