const dom = document.getElementById("demo");


var string = "yoo";
var num = 40;
var room = {dimension: "2x2", color:"red", location:"Adidome"};
// array
var locations = ["Accra", "Kumerica", "Highman", "Taadi"];
locations.push("Kpeve");
locations[2] = 300;
locations.pop();
locations.splice(2, 0, "Ho");
locations.forEach(
    location => dom.innerHTML += `${location} is a location <br>`
);

// dom.innerText = room.color;


// dom.innerText += typeof num +"\n";
// dom.innerText += locations;

function rent(duration, mcost){
    console.log(duration+mcost);
}

rent(12,1200)