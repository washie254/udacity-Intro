var secretWeapon = 1;

function mansionUp() {
    var chest = prompt("A chest is in the upper room. Do you dare to open it? Enter yes or no.").toUpperCase();
   
    switch(chest) {
        case "YES":
            alert("There are jewels in this chest. You take them home. Now you are rich. Game Over.");
        break;
        case "NO":
            alert("Foolish choice. The chest and all the treasures in it disappear forever, and are you locked in the room. Game Over.");
        break;
        default:
            alert("Please enter yes or no.");
    }
}

function leftEnterMansion() {
    var downOrUp = prompt("There is a staircase leading upstairs and a staircase leading downstairs. Which one do you choose? Enter up or down.").toUpperCase();
   
    switch(downOrUp) {
        case "UP":
            mansionUp();
        break;
        case "DOWN":
            alert("Uh oh. Looks like there's a pit of lava in the basement. You are never heard from again.");
        break;
        default:
            alert("Please enter up or down.");
        downOrUp();
    }
}

function leftFarther() {
    var goBack = prompt("You find a chest of jewels. Now do you want to go home? Enter home or farther.").toUpperCase();
   
    switch(goBack) {
        case "HOME":
            alert("Wise choice. You sell the jewels and become a billionaire.");
        break;
        case "FARTHER":
            alert("You lose your way. Game Over.");
        break;
        default:
            alert("Please enter home or farther.");
            goBack();
    }   
}

function defeatBear() {
    var goFarther = prompt("Do you want to go farther or go home and sell the bear skin? Enter home or farther.").toUpperCase();
   
    switch(goFarther) {
        case "HOME":
            alert("You sell the bear skin for half as much as you had hoped. You regret your decision.");
        break;
        case "FARTHER":
            leftFarther();
        break;
        default:
            alert("Please enter home or farther.");
            goFarther();
    }
}

function leftSafe() {
    var weaponChoice = prompt("A wild bear appears on the trail! Luckily you have a secret weapon. It can be used 1 time. Do you use it? Enter yes or no.").toUpperCase();
   
    switch(weaponChoice) {
        case "YES":
            alert("Excellent. You defeated the bear.");
            secretWeapon--;
            defeatBear();
        break;
        case "NO":
            alert("Oops. The bear got you.");
        break;
        default:
            alert("Please enter yes or no.");
        leftSafe();
    }
}

function goLeft() {
    var mansionChoose = prompt("You choose left. A few miles down the road, an abandoned stone mansion appears! Do you want to go in? Enter yes or no.").toUpperCase();
   
    switch(mansionChoose) {
        case "YES":
            leftEnterMansion();
        break;
        case "NO":
            leftSafe();
        break;
        default:
            alert("Please enter yes or no");
        goLeft();
    }
}

function wolfGone() {
    alert("The wolf is gone. You have safely survived an encounter with a creature in this forest. You become famous.");
}

function findWolf() {
    var useWeapon = prompt("You find a wolf! Do you choose to use your secret weapon? It can only be used once. Enter yes or no.").toUpperCase();
   
    switch(useWeapon) {
        case "YES":
            alert("The wolf flings the weapon back at you! Game Over");
        break;
        case "NO":
            alert("Good choice. The wolf passes by.");
            wolfGone();
        break;
        default:
            alert("Please enter yes or no.");
    }
}

function grabSwamp() {
    alert("Excellent decision. You safely float to the other side.");
    findWolf();
}

function swimSwamp() {
    alert("Why did you swim? This swamp is alligator infested! Game Over.");   
}

function fallSwamp() {
    var swim = prompt("The bridge breaks! Do you swim to the other side or grab on to a floating piece of wood? Enter grab or swim.").toUpperCase();
   
    switch(swim) {
        case "SWIM":
            swimSwamp();
        break;
        case "GRAB":
            grabSwamp();
        break;
        default:
            alert("Please enter grab or swim.");
        break;
    }
}

function rightSafe() {
    var caveChoose = prompt("A cave appears. Do you enter it? Yes or no.").toUpperCase();
   
    switch(caveChoose) {
        case "YES":
            enterCave();
        break;
        case "NO":
            noCave();
        break;
        default:
            alert("Please enter yes or no.");
        break;
    }   
}

function enterCave() {
    alert("It's dark. You find a lantern and light it. You wander around but get lost. Game Over.");   
}

function noCave() {
    var onward = prompt("Do you want to go farther? Enter yes or no.").toUpperCase();
   
    switch(onward) {
        case "YES":
            alert("Now you're lost. Game Over.");
        break;
        case "NO":
            alert("I'm proud of you. You made the right choice. You Win!");
        break;
        default:
            alert("Please enter yes or no.");
        break;
    }
}

function goRight() {
    var bridgeChoose = prompt("A few minutes down the trail, a swamp appears. There is a rickety bridge leading across. Do you cross it? Enter yes or no.").toUpperCase();
   
    switch(bridgeChoose) {
        case "YES":
            fallSwamp();
        break;
        case "NO":
            rightSafe();
        break;
        default:
            alert("Please enter yes or no");
        goRight();
    }   
}

function adventure() {
    var leftOrRight = prompt("You are trekking through a forest. You come to a fork in the road. Do you go left or right?").toUpperCase();
   
    switch(leftOrRight) {
        case "LEFT":
            goLeft();
        break;
        case "RIGHT":
            goRight();
        break;
        default:
            alert("Please enter either left or right");
            adventure();
    }
}

adventure();