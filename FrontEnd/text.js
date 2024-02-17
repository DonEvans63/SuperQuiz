$(() => {
  let $next = $('.next');
  let $cover = $('.cover');
  let $divQuestion = $('.divQuestion');
  let $playBtn = $('.playBtn');
  let $paragraphs = $('.paragraphs');
  let $addYourQuest = $('#addYourQuest');
  let $toAddBtn = $('#toAddBtn');
  let $tryAgain = $('.tryAgain');
  let $response = $('.response');
  let $result = $('.result');
  let $start = $('.start');
  let $addAnotherQuestion = $('.addAnotherQuestion');
  let currentCorrectAns;
  let btnArray = [document.getElementById('btnA'), document.getElementById('btnB'), document.getElementById('btnC'), document.getElementById('btnD')]; //Gives each btn in the actual quiz an index

  let score = 0;
  let quizQuestions = [];
  let quizAnswers = [];
  let quizCorrect = [];
  let randomSet = new Set();
  let usedSet = new Set();

  $addYourQuest.hide();//hides the question adding display on initiation
  $('.next').attr('disabled', true); // sets next question btn on quiz to disabled on initiation

  // function that starts the quiz
  function startQuiz() {
    score = 0;
    quizQuestions = [];
    quizAnswers = [];
    quizCorrect = [];
    randomSet = new Set();
    $result.hide();
  }

  class Question {
    constructor(q, answer, correct) {
      this.q = q,
        this.answer = answer,
        this.correct = correct;
    }
  }
  console.log(startQuiz)
  // Bank of of fourty quiz questions
  const questionBank = [
    new Question('What is the capitol of Oregon?', ['Salem', 'Portland', 'Eugene', 'Medford'], 0),
    new Question('Who was the founder of the Sierra Club?', ['Sam Snead', 'John Muir', 'Bob Dilps', 'Ralph W. Emmerson'], 1),
    new Question('In what country is the deepest freshwater lake located?', ['Russia', 'China', 'Peru', 'Pakistan'], 0),
    new Question('Who won the World Series in 1988?', ['Giants', 'Yankees', 'Braves', 'Dodgers'], 3),
    new Question('In what year did man first step foot on the moon?', [1967, 1968, 1969, 1970], 2),
    new Question('From what country does quinoa and the potato originate?', ['USA', 'Peru', 'Hawaii', 'Ireland'], 1),
    new Question('In what year was Alaska admitted into the United States?', [1948, 1953, 1956, 1959], 3),
    new Question('Which T.V series had the largest audiance for its final episode?', ['Mash', 'Friends', 'Seinfeld', 'Cheers'], 0),
    new Question('Who sang the song Pencil Neck Geek?', ['Freddie Blassy', 'Phinnias P. Quimby', 'Zeke Moab Jr.', 'Homer Frisbe'], 0),
    new Question('In what year did Folsom State Prison open?', [1850, 1873, 1880, 1902,], 2),
    new Question('Which city is the furthest west?', ['Los Angeles', 'Salt Lake City', 'Reno', 'Boise Idaho'], 2),
    new Question('What European country is threatened by over 100 active volcanoes?', ['Italy', 'Iceland', 'Spain', 'Norway'], 1),
    new Question('In horse racing what word is used to describe an eighth of a mile?', ['Furloung', 'Length', 'Phathom', 'Stretch'], 0),
    new Question('What\'s the state bird of record in seven US states?', ['Golden Eagle', 'Turkey', 'Falcon', 'Cardinal'], 3),
    new Question('Which is not a city in Germany?', ['Bonn', 'Frankfurt', 'Brussels', 'Berlin'], 2),
    new Question('What\'s the only New England state without a seacoast?', ['Conneticut', 'Vermont', 'Rhode Island', 'Delaware'], 1),
    new Question('What painter died penniless in the arms of his brother?', ['Vincent van Gogh', 'Monet', 'Leonardo da Vinci', 'Andy Warhol'], 0),
    new Question('Who, two weeks earlier, slept in the same bed that Abraham Lincoln died in?', ['Robrt E. Lee', 'Ulysses S. Grant', 'Teddy Roosevelt', 'John Wilkes Booth'], 3),
    new Question('What nation has has a monarchy the longest?', ['Great Britain', 'Norway', 'Japan', 'Denmark'], 2),
    new Question('What island country tops the tea consumption per capita?', ['Ireland', 'Taiwan', 'Cuba', 'Japan'], 0),
    new Question('Who was the only American to become vice president and president after resignations?', ['Gerald Ford', 'Teddy Rosavelt', 'Warren Harding', 'Lyndon Johnson'], 0),
    new Question('What do you call the offspring of a male tiger and female lion?', ['Liger', 'Ligon', 'Tiglon', 'Tigler'], 2),
    new Question('What does MI stand for in the spy business?', ['Master Investigator', 'Military Intelligance', 'Mystery Investigations', 'Managed Intelligence'], 1),
    new Question('How many designated face-off spots are there on a hockey rink?', ['Five', 'Six', 'Seven', 'Nine'], 3),
    new Question('What Arizona lake is found behind the parker dam?', ['Lake Mead', 'Lake Havasu', 'Lake Mojave', 'Lake Parker'], 1),
    new Question('What was the largest number of ex-presidents living at one time?', ['Four', 'Five', 'Six', 'Seven'], 1),
    new Question('What New England state made whistling under water illegal?', ['Maine', 'Conneticut', 'New Hampshire', 'Vermont'], 3),
    new Question('What holiday is celebrated in Canada on the second Monday in October?', ['Thanksgiving', 'Veteran\'s Day', 'Independence Day', 'Halloween'], 0),
    new Question('What\'s the southern most state capitol among the 48 contiguous states?', ['Miami', 'Mobile', 'Austin', 'Savanah'], 2),
    new Question('Who\'s the only person to be elected twice as vice-president and twice as president?', ['Gerald Ford', 'Franklin Roosevelt', 'Dwight Eisenhower', 'Richard Nixon'], 3),
    new Question('What Canadian was dubbed the "the Godfather of grunge"?', ['Brian Adams', 'Eddie Vetter', 'Neil Young', 'David Crosby'], 2),
    new Question('What southern city did Andrew Jackson name for one on the Nile?', ['Savanah', 'Memphis', 'Augusta', 'Athens'], 1),
    new Question('What South American country boasts the highest golf course and ski run?', ['Columbia', 'Argentina', 'Chile', 'Bolivia'], 3),
    new Question('What\'s the most venomous snake is the US?', ['Rattle Snake', 'Water Macason', 'Cotton Mouth', 'Coral Snake'], 3),
    new Question('What sea contains Europes lowest point?', ['Adriatic', 'Baltic', 'Caspian', 'Mediterainean'], 2),
    new Question('How many years did the average ancient Roman live?', ['22', '28', '32', '42'], 0),
    new Question('What\'s the only country where whooping cranes breed in the wild?', ['Japan', 'Kenya', 'Canada', 'US'], 2),
    new Question('What Kraft product did US houeholds find over 1300 hundred uses for in 1952?', ['Ketchup', 'Cheez Wiz', 'Mayonnaise', 'Tarter Sauce'], 1),
    new Question('What do you call a weasel whose coat turns white in the winter?', ['Ferret', 'Mongoose', 'Ermine', 'Skink'], 2),
    new Question('What Scandinavian country are you in when you\'re vacationing in Hell?', ['Norway', 'Finland', 'Sweden', 'Denmark'], 0)
  ];

  /*Creates random number Set to both choose 10 quiz questions and ensure that the same questions are not used twice for three quiz rotations. It then clears the usedSet and uses the entire question bank to start new three quiz rotation */
  function createRandomQuestionOrder() {
    if (usedSet.size === 40) {
      usedSet.clear();
    }
    while (randomSet.size < 10) {
      let randNum = Math.floor(Math.random() * questionBank.length);
      if (!usedSet.has(randNum)) {
        randomSet.add(randNum);
      }
    }
  }

  function showQuiz() {
    $divQuestion.show();
    $next.show();
    $paragraphs.show();
    $result.show();
  }

  function hideQuiz() {
    $divQuestion.hide();
    $next.hide();
    $paragraphs.hide();
    $result.hide();
    $tryAgain.hide();
    $addAnotherQuestion.hide();
  }

  /*Creates current question by pushing the value in the randomSet into the quizQueations, quizAnswers, and quizCor arrays. It also adds the same random set values into the used set for creareRandomQuestionOrder function*/
  function currentQuestion() {
    for (let value of randomSet) {
      quizQuestions.push(questionBank[value].q);
      quizAnswers.push(questionBank[value].answer[0]);
      quizAnswers.push(questionBank[value].answer[1]);
      quizAnswers.push(questionBank[value].answer[2]);
      quizAnswers.push(questionBank[value].answer[3]);
      quizCorrect.push(questionBank[value].correct);
      usedSet.add(value);
    }
  }

  //Displays the quizQuestion, quizAnswers,and quizCor index[0] onto the page using the shift() method
  function showQuestion() {
    $('.divQuestion').text(`${quizQuestions.shift()}`);
    $('#item1').text(`${quizAnswers.shift()}`);
    $('#item2').text(`${quizAnswers.shift()}`);
    $('#item3').text(`${quizAnswers.shift()}`);
    $('#item4').text(`${quizAnswers.shift()}`);
    currentCorrectAns = quizCorrect.shift();
  }

  // Grabs the input values from the addYourQuestion form and adds them to the questionBank using the submit btn
  $('#addYourQuest').on('submit', function (e) {
    e.preventDefault();
    let $enterQuest = $('#enterQuest').val();
    let $enterAns1 = $('#enterAns1').val();
    let $enterAns2 = $('#enterAns2').val();
    let $enterAns3 = $('#enterAns3').val();
    let $enterAns4 = $('#enterAns4').val();
    let $enterCor = Math.floor($('#enterCor').val() - 1);
    let addQ = new Question($enterQuest, [$enterAns1, $enterAns2, $enterAns3, $enterAns4], $enterCor);
    questionBank.push(addQ);
    $(':input').val('');
  });

  // The start quiz btn
  $start.on('click', function () {
    $addYourQuest.addClass("hidden");
    showQuiz();
    runTheQuiz();
  });


  // The play now btn on initiattion page
  $playBtn.on('click', function () {
    $cover.hide();
    showQuiz();
    $addYourQuest.hide();
    runTheQuiz();
  });

  // The click to add your question on initiation page
  $toAddBtn.on('click', function () {
    $addYourQuest.removeClass("hidden");
    $cover.hide();
  });

  // Compares correct question answers to question btn indices displaying Correct or Incorrect depending on your btn choice
  $('.answer').on('click', function (e) {
    $('.next').attr('disabled', false);
    $('.answer').attr('disabled', true);
    if (currentCorrectAns === btnArray.indexOf(e.target)) {
      score++;
      $response.text('Correct!');
    } else {
      $response.text('Incorrect!');
    }
  });


  // Advances quiz to next question and displays quiz results at the completion of 10 questions
  $('.next').on('click', function () {
    $('.answer').attr('disabled', false);
    $('.next').attr('disabled', true);
    if (quizQuestions.length > 0) {
      showQuestion();
      $response.text('');
      $divQuestion.show();
    } else if (quizQuestions.length === 0) {
      $next.hide();
      $result.show();
      $tryAgain.show();
      $addAnotherQuestion.show();
      $response.text('');
      $divQuestion.hide();
      $paragraphs.hide();
      $result.text(`You scored ${score} out of 10 on the quiz!`);
    }
  });

  //  At completion of the quiz clicking on this btn returns user to add your question form
  $addAnotherQuestion.on('click', function () {
    hideQuiz();
    $addYourQuest.removeClass("hidden");;
    runTheQuiz();
    $tryAgain.hide();
  });

  // At completion of quiz this btn allows user to take the quiz again
  $tryAgain.on('click', function () {
    showQuiz();
    $addYourQuest.hide();
    runTheQuiz();
    $tryAgain.hide();
    $addAnotherQuestion.hide();
  });

  // This is the function that runs the quiz
  function runTheQuiz() {
    startQuiz();
    createRandomQuestionOrder();
    currentQuestion();
    showQuestion();
  }

  hideQuiz();

});



const newLocal = new Target();
const newTarget = newLocal;
let randomSet = new Set();
let usedSet = new Set();
let targetArray = [newTarget, newTarget, '//ten times'];


function createRandomTarget() {
  if (usedSet.size === 40) {
    usedSet.clear();
  }
  while (randomSet.size < 10) {
    let randNum = Math.floor(Math.random() * targetArray.length);
    if (!usedSet.has(randNum)) {
      randomSet.add(randNum);
    }
  }
}
