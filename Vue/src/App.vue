<template>
    <body>
        <h1> Chess Game Time !  </h1>
        <h3> Are You Ready To Play ?</h3>
        <board />
    </body>

</template>

<script>
    import board from './components/board.vue'

export default {
  name: 'App',
        components: {
            board
        }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
