<template>
    <div class="test">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width-device-wdith, initial-scale=1.0" />
            <link rel="stylesheet" href="./style.css" />
            <title>Chess Board Design </title>
        </head>
        <body>
            <h1> Chess Game Time !  </h1>
            <h3> Are You Ready To Play ?</h3>
            <div class="upperdiv">
                <div class="numbers"></div>
                <div class="letters"></div>
            </div>
            <div class="board"></div>
            <scr></scr>
        </body>
    </div>
</template>

<script>
    const board = document.querySelector(".board");
    const boardletters = document.querySelector(".letters");
    const boardnumbers = document.querySelector(".numbers");
    let letters = ["A", "B", "C", "D", "E", "F", "G", "H"];
    let index = 0;
    let beige = false;
    let num = 1;


    for (let i = 0; i < 8; i++) {
        let letter = document.createElement("li");
        letter.textContent = letters[i];
        boardletters.appendChild(letter);

        let numbers = document.createElement("li");
        numbers.textContent = num++;
        boardnumbers.appendChild(numbers);
    }

    for (let i = 1; i <= 64; i++) {
        const square = document.createElement("div");
        if (beige) {
            square.classList.add("square");
            square.classList.add("beige");
            index++;
            beige = !beige;
        }
        else {
            square.classList.add("square");
            square.classList.add("sandybrown");
            index++;
            beige = !beige;
        }

        board.appendChild(square);
        if (index === 8) {
            beige = !beige;
            index = 0;
        }
    }

export default {
       name: 'test'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
