// Back-end (JavaScript):

const button = document.getElementById('button');
const wordsDiv = document.getElementById('words');

button.addEventListener('click', () => {
  fetch('words.json')
    .then(res => res.json())
    .then(words => {
      const randomWords = getRandomWords(words, 3); // get 3 random words from the array
      wordsDiv.innerHTML = randomWords.join(', ');
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
