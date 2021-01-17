<template>
  <chessBoard />
</template>

<script>
    export default {
        name: 'chessSquare',
        props: {
            row: Number,
            col: Number,
            show: Boolean
        }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .square img {
    width: 80px;
    height: 80px;
    object-fit: cover;
    grid-row-gap: 0;
    
  }
  .parent {
    position: relative;
    top: 0;
    left: 0;
    width: 80px;
    height: 80px;
  }
  .black {
    width: 80px;
    height: 80px;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -o-user-select: none;
    user-select: none;
  }

  .over {
    position: relative;
    top: 0;
    left: 0;
    border: 1px solid #000000;
    width: 80px;
    height: 80px;
    -khtml-user-select: none;
    -o-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
  }

  .under {
    position: absolute;
    top: -80px;
    left: -0px;
    border: 1px solid #000000;
    width: 80px;
    height: 80px;
    -khtml-user-select: none;
    -o-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
  }
</style>

