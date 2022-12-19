// Declare variables
var timeunit = 1; //Time Unit
var verbage = 2; //Verbs
var item = 3; //Items
var nouns = 4; //Nouns
var emotion = "Pringle"; //Emotions
var ln = 1; //Lower limit for time
var un= 60; //Upper limit for time

//Randomiser
/*var array = [
    ["Mango","M"],
    ["Lychee","L"],
    ["Pineapple","P"],
    ["Banana","B"]
];
var randomItem = array[Math.random() * array.length | 0];
*/

const greetings = ['Howdy', 'Bonjour', 'Hello', 'Dude']

const greeting = greetings[  
  Math.floor(Math.random() * greetings.length)
]

var x = "Hello ";
var y = "World!";




//Print
//const x = `hello ${emotion}`;

// Import
// Setup
// Loop
// Pull Data and Assign Index Numbers
// Generate Words
// Print




var jsonContent = {
  "featured": [
      {
          "id": "111",
          "title": "post title 111",
          "desc": "This is a test desc 111"
      },
      {
          "id": "222",
          "title": "post title 222",
          "desc": "This is a test desc 222"
      },
      {
          "id": "333",
          "title": "post title 333",
          "desc": "This is a test desc 333"
      }
  ]
}

var random = jsonContent.featured[Math.floor(Math.random() * jsonContent.featured.length)];
console.log(random)

var random = jsonContent["featured"][Math.floor(Math.random()*jsonContent["featured"].length)];


var rawdata = fs.readFileSync('/../list.json');
  var jsonlist = JSON.parse(rawdata);

  var randomNum = Math.round(Math.random() * (1 + 1169) - 1);

  var pokemon = pokemon2[randomNum];

  console.log(pokemon);
  console.log(typeof(pokemon));

  res.json(pokemon);

  var json = JSON.stringify(arr);
alert(json);

//const x = console.log(jsonlist["timeunit"][Math.floor(Math.random()*jsonContent["featured"].length)]);




$.get('/../list.json')
  .done(data => {
    console.log(data);
    const parseData = JSON.parse(data);
    console.log(parseData.timevalues);
  });

fetch('/../list.json')
  .then(data => data.json())
  .then(data => {
    console.log(data);
 });