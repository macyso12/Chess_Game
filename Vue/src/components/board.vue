<template>
    <div class="board">
        <div v-for="index in 5" :key="index">
            <chessSquare color= "{{index}}" />
        </div>
    </div>
</template>

<script>
    import chessSquare from './chessSquare.vue'

export default {
    name: 'board',
    components: {
        chessSquare
        }
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
