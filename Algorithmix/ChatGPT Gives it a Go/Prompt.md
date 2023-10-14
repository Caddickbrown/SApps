can you give me the code to create a web app allows me to press a button and multiple random words are displayed from a separate JSON file? Please use HTML for the front-end and JavaScript for the back-end

Certainly! Here is an example of a web app that allows you to press a button to display multiple random words from a separate JSON file using HTML for the front-end and JavaScript for the back-end:

Copy code
<!— Front-end (HTML): —>

<!DOCTYPE html>
<html>
  <head>
    <title>Random Words</title>
  </head>
  <body>
    <button id=“button”>Generate Words</button>
    <div id=“words”></div>

    <script src=“app.js”></script>
  </body>
</html>
Copy code
// Back-end (JavaScript):

const button = document.getElementById(‘button’);
const wordsDiv = document.getElementById(‘words’);

button.addEventListener(‘click’, () => {
  fetch(‘words.json’)
    .then(res => res.json())
    .then(words => {
      const randomWords = getRandomWords(words, 3); // get 3 random words from the array
      wordsDiv.innerHTML = randomWords.join(‘, ‘);
    });
});

function getRandomWords(words, num) {
  const shuffled = shuffle(words);
  return shuffled.slice(0, num);
}

function shuffle(array) {
  let currentIndex = array.length;
  let temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (currentIndex !== 0) {
    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}
The words.json file should contain an array of words, like this:

Copy code
[  “apple”,  “banana”,  “orange”,  “grape”,  “strawberry”]

When the button is clicked, the app will fetch the words.json file, select 3 random words from the array, and display them in the words div.